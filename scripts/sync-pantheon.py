#!/usr/bin/env python3
"""
Sync framework stats from Pantheon data.
Extracts top 10 from each dashboard (Science/General × Daily/Projects).
"""

import json
from pathlib import Path
from datetime import datetime

# Paths
PANTHEON_DIR = Path("/root/pantheon-data/status")
OUTPUT_FILE = Path("/root/awesome-agents-design/data/stats.json")
FRAMEWORKS_DIR = Path("/root/awesome-agents-design/docs/frameworks")

def load_pantheon_data():
    """Load current and change data for Science and General."""
    science_current = json.loads((PANTHEON_DIR / "science_data_current.json").read_text())
    science_change = json.loads((PANTHEON_DIR / "science_data_change.json").read_text())
    general_current = json.loads((PANTHEON_DIR / "general_data_current.json").read_text())
    general_change = json.loads((PANTHEON_DIR / "general_data_change.json").read_text())
    
    return {
        "science": {"current": science_current, "change": science_change},
        "general": {"current": general_current, "change": general_change}
    }

def merge_stats(current, change):
    """Merge current stats with daily change."""
    # Create lookup for change data
    change_lookup = {item["name"]: item for item in change}
    
    merged = []
    for item in current:
        name = item["name"]
        daily = change_lookup.get(name, {})
        
        # Get daily stars (from change data)
        daily_stars = daily.get("stars", 0)
        # Handle case where change equals current (new repo or no previous data)
        if daily_stars == item["stars"] and item["stars"] > 100:
            daily_stars = 0  # Likely a new entry, set daily to 0
        
        merged.append({
            "name": name,
            "url": item.get("url", f"https://github.com/{name}"),
            "stars": item["stars"],
            "daily_stars": daily_stars,
            "forks": item["forks"],
            "issues": item["open_issues"],
            "language": item.get("language", "Unknown"),
            "last_commit": item.get("last_commit", ""),
            "contributors": item.get("contributors", 0),
            "commits": item.get("commits", 0),
        })
    
    return merged

def get_dashboard_top10(data, category):
    """Get top 10 for Projects (total stars) and Daily (daily stars)."""
    merged = merge_stats(data["current"], data["change"])
    
    # Projects Dashboard: sort by total stars
    projects_top10 = sorted(merged, key=lambda x: x["stars"], reverse=True)[:10]
    
    # Daily Dashboard: sort by daily stars
    daily_top10 = sorted(merged, key=lambda x: x["daily_stars"], reverse=True)[:10]
    
    return {
        f"{category}_projects": projects_top10,
        f"{category}_daily": daily_top10
    }

def deduplicate(all_frameworks):
    """Remove duplicates, keeping highest stats."""
    seen = {}
    for fw in all_frameworks:
        name = fw["name"]
        if name not in seen:
            seen[name] = fw
        else:
            # Keep the one with higher stars
            if fw["stars"] > seen[name]["stars"]:
                seen[name] = fw
    
    return list(seen.values())

def main():
    print(f"[{datetime.now()}] Loading Pantheon data...")
    data = load_pantheon_data()
    
    print(f"[{datetime.now()}] Extracting top 10 from each dashboard...")
    
    # Get top 10 from each dashboard
    science_dashboards = get_dashboard_top10(data["science"], "science")
    general_dashboards = get_dashboard_top10(data["general"], "general")
    
    # Combine all unique frameworks
    all_frameworks = (
        science_dashboards["science_projects"] +
        science_dashboards["science_daily"] +
        general_dashboards["general_projects"] +
        general_dashboards["general_daily"]
    )
    
    # Deduplicate
    unique_frameworks = deduplicate(all_frameworks)
    
    print(f"[{datetime.now()}] Found {len(unique_frameworks)} unique frameworks")
    
    # Add category
    for fw in unique_frameworks:
        if fw["name"] in [f["name"] for f in science_dashboards["science_projects"]]:
            fw["category"] = "science"
        elif fw["name"] in [f["name"] for f in general_dashboards["general_projects"]]:
            fw["category"] = "general"
        else:
            # Infer from context
            fw["category"] = "other"
    
    # Build output JSON
    output = {
        "last_updated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "dashboards": {
            "science_projects": [
                {"name": fw["name"], "stars": fw["stars"], "daily_stars": fw["daily_stars"]}
                for fw in science_dashboards["science_projects"]
            ],
            "science_daily": [
                {"name": fw["name"], "stars": fw["stars"], "daily_stars": fw["daily_stars"]}
                for fw in science_dashboards["science_daily"]
            ],
            "general_projects": [
                {"name": fw["name"], "stars": fw["stars"], "daily_stars": fw["daily_stars"]}
                for fw in general_dashboards["general_projects"]
            ],
            "general_daily": [
                {"name": fw["name"], "stars": fw["stars"], "daily_stars": fw["daily_stars"]}
                for fw in general_dashboards["general_daily"]
            ],
        },
        "frameworks": unique_frameworks,
        "summary": {
            "total_frameworks": len(unique_frameworks),
            "total_stars": sum(fw["stars"] for fw in unique_frameworks),
            "most_popular": max(unique_frameworks, key=lambda x: x["stars"])["name"],
            "fastest_growing": max(unique_frameworks, key=lambda x: x["daily_stars"])["name"],
            "highest_daily_stars": max(fw["daily_stars"] for fw in unique_frameworks),
        }
    }
    
    # Write output
    OUTPUT_FILE.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"[{datetime.now()}] Written to {OUTPUT_FILE}")
    
    # Print summary
    print("\n=== Summary ===")
    print(f"Most Popular: {output['summary']['most_popular']}")
    print(f"Fastest Growing: {output['summary']['fastest_growing']}")
    print(f"Highest Daily Stars: {output['summary']['highest_daily_stars']}")
    
    # Print dashboard top 10s
    print("\n=== Science - Projects Dashboard (Top 10) ===")
    for i, fw in enumerate(output["dashboards"]["science_projects"], 1):
        print(f"{i}. {fw['name']}: {fw['stars']} stars (+{fw['daily_stars']}/day)")
    
    print("\n=== Science - Daily Dashboard (Top 10) ===")
    for i, fw in enumerate(output["dashboards"]["science_daily"], 1):
        print(f"{i}. {fw['name']}: +{fw['daily_stars']}/day ({fw['stars']} total)")
    
    print("\n=== General - Projects Dashboard (Top 10) ===")
    for i, fw in enumerate(output["dashboards"]["general_projects"], 1):
        print(f"{i}. {fw['name']}: {fw['stars']} stars (+{fw['daily_stars']}/day)")
    
    print("\n=== General - Daily Dashboard (Top 10) ===")
    for i, fw in enumerate(output["dashboards"]["general_daily"], 1):
        print(f"{i}. {fw['name']}: +{fw['daily_stars']}/day ({fw['stars']} total)")

if __name__ == "__main__":
    main()