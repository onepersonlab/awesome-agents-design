#!/usr/bin/env python3
"""
Sync framework stats from OnePersonLab Website data.
Extracts top 10 from each dashboard (Research/General × Projects/Daily).
"""

import json
from pathlib import Path
from datetime import datetime

# Paths
ONEPERSONLAB_DIR = Path("/root/onepersonlab-website/data")
OUTPUT_FILE = Path("/root/awesome-agents-design/data/stats.json")

def load_data():
    """Load Research and General agent data."""
    research_update = json.loads(
        (ONEPERSONLAB_DIR / "Research-agent-list-update.json").read_text()
    )
    general_update = json.loads(
        (ONEPERSONLAB_DIR / "General-agent-list-update.json").read_text()
    )
    
    return {
        "research": research_update["repos"],
        "general": general_update["repos"]
    }

def get_dashboard_top10(repos, category):
    """Get top 10 for Projects (total stars) and Daily (weekly stars)."""
    
    # Projects Dashboard: sort by total stars
    projects_top10 = sorted(repos, key=lambda x: x["stars"], reverse=True)[:10]
    
    # Daily Dashboard: sort by weekly stars
    daily_top10 = sorted(repos, key=lambda x: x.get("weeklyStars", 0), reverse=True)[:10]
    
    return {
        f"{category}_projects": projects_top10,
        f"{category}_daily": daily_top10
    }

def deduplicate(all_frameworks):
    """Remove duplicates, keeping highest stats."""
    seen = {}
    for fw in all_frameworks:
        name = fw["full_name"]
        if name not in seen:
            seen[name] = fw
        else:
            # Keep the one with higher stars
            if fw["stars"] > seen[name]["stars"]:
                seen[name] = fw
    
    return list(seen.values())

def format_framework(fw):
    """Format framework data for output."""
    return {
        "name": fw["full_name"],
        "url": fw.get("url", f"https://github.com/{fw['full_name']}"),
        "stars": fw["stars"],
        "weekly_stars": fw.get("weeklyStars", 0),
        "forks": fw.get("forks", 0),
        "language": fw.get("language", "Unknown"),
        "description": fw.get("description", "")[:100],
        "updated": fw.get("updated", ""),
    }

def main():
    print(f"[{datetime.now()}] Loading OnePersonLab data...")
    data = load_data()
    
    print(f"[{datetime.now()}] Research repos: {len(data['research'])}")
    print(f"[{datetime.now()}] General repos: {len(data['general'])}")
    
    # Get top 10 from each dashboard
    research_dashboards = get_dashboard_top10(data["research"], "research")
    general_dashboards = get_dashboard_top10(data["general"], "general")
    
    # Combine all unique frameworks
    all_frameworks = (
        research_dashboards["research_projects"] +
        research_dashboards["research_daily"] +
        general_dashboards["general_projects"] +
        general_dashboards["general_daily"]
    )
    
    # Deduplicate
    unique_frameworks = deduplicate(all_frameworks)
    formatted_frameworks = [format_framework(fw) for fw in unique_frameworks]
    
    # Add category
    research_names = [fw["full_name"] for fw in research_dashboards["research_projects"]]
    general_names = [fw["full_name"] for fw in general_dashboards["general_projects"]]
    
    for fw in formatted_frameworks:
        if fw["name"] in research_names:
            fw["category"] = "research"
        elif fw["name"] in general_names:
            fw["category"] = "general"
        else:
            fw["category"] = "other"
    
    print(f"[{datetime.now()}] Found {len(formatted_frameworks)} unique frameworks")
    
    # Build output JSON
    output = {
        "last_updated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "OnePersonLab Website (https://github.com/onepersonlab/onepersonlab-website)",
        "dashboards": {
            "research_projects": [
                {
                    "name": fw["full_name"],
                    "stars": fw["stars"],
                    "weekly_stars": fw.get("weeklyStars", 0),
                    "language": fw.get("language", "Unknown"),
                }
                for fw in research_dashboards["research_projects"]
            ],
            "research_daily": [
                {
                    "name": fw["full_name"],
                    "stars": fw["stars"],
                    "weekly_stars": fw.get("weeklyStars", 0),
                    "language": fw.get("language", "Unknown"),
                }
                for fw in research_dashboards["research_daily"]
            ],
            "general_projects": [
                {
                    "name": fw["full_name"],
                    "stars": fw["stars"],
                    "weekly_stars": fw.get("weeklyStars", 0),
                    "language": fw.get("language", "Unknown"),
                }
                for fw in general_dashboards["general_projects"]
            ],
            "general_daily": [
                {
                    "name": fw["full_name"],
                    "stars": fw["stars"],
                    "weekly_stars": fw.get("weeklyStars", 0),
                    "language": fw.get("language", "Unknown"),
                }
                for fw in general_dashboards["general_daily"]
            ],
        },
        "frameworks": formatted_frameworks,
        "summary": {
            "total_frameworks": len(formatted_frameworks),
            "total_stars": sum(fw["stars"] for fw in formatted_frameworks),
            "most_popular": max(formatted_frameworks, key=lambda x: x["stars"])["name"],
            "fastest_growing": max(formatted_frameworks, key=lambda x: x["weekly_stars"])["name"],
            "highest_weekly_stars": max(fw["weekly_stars"] for fw in formatted_frameworks),
        }
    }
    
    # Write output
    OUTPUT_FILE.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"[{datetime.now()}] Written to {OUTPUT_FILE}")
    
    # Print summary
    print("\n=== Summary ===")
    print(f"Most Popular: {output['summary']['most_popular']}")
    print(f"Fastest Growing: {output['summary']['fastest_growing']}")
    print(f"Highest Weekly Stars: {output['summary']['highest_weekly_stars']}")
    
    # Print dashboard top 10s
    print("\n=== Research - Projects Dashboard (Top 10) ===")
    for i, fw in enumerate(output["dashboards"]["research_projects"], 1):
        print(f"{i}. {fw['name']}: {fw['stars']} stars (+{fw['weekly_stars']}/week)")
    
    print("\n=== Research - Daily Dashboard (Top 10) ===")
    for i, fw in enumerate(output["dashboards"]["research_daily"], 1):
        print(f"{i}. {fw['name']}: +{fw['weekly_stars']}/week ({fw['stars']} total)")
    
    print("\n=== General - Projects Dashboard (Top 10) ===")
    for i, fw in enumerate(output["dashboards"]["general_projects"], 1):
        print(f"{i}. {fw['name']}: {fw['stars']} stars (+{fw['weekly_stars']}/week)")
    
    print("\n=== General - Daily Dashboard (Top 10) ===")
    for i, fw in enumerate(output["dashboards"]["general_daily"], 1):
        print(f"{i}. {fw['name']}: +{fw['weekly_stars']}/week ({fw['stars']} total)")

if __name__ == "__main__":
    main()