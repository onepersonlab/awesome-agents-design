#!/bin/bash
# Update stats.json from GitHub API
# Run: ./scripts/update-stats.sh

set -e

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DATA_FILE="$REPO_DIR/data/stats.json"
LOG_FILE="$REPO_DIR/logs/update-$(date +%Y%m%d).log"

# GitHub Token (from environment or git-credentials)
if [ -z "$GITHUB_TOKEN" ]; then
  GITHUB_TOKEN=$(grep -o 'ghp_[^@]*' ~/.git-credentials 2>/dev/null | head -1)
fi

if [ -z "$GITHUB_TOKEN" ]; then
  echo "ERROR: No GitHub token found. Set GITHUB_TOKEN env or configure ~/.git-credentials"
  exit 1
fi

# Create logs directory
mkdir -p "$REPO_DIR/logs"

echo "[$(date)] Starting stats update..." | tee "$LOG_FILE"

# Frameworks to track
FRAMEWORKS=(
  "aiming-lab/AutoResearchClaw:research"
  "wentorai/Research-Claw:research"
  "sakana-ai/AI-Scientist:research"
  "microsoft/autogen:general"
  "geekan/MetaGPT:general"
  "crewAIInc/crewAI:general"
  "langchain-ai/langgraph:general"
  "openai/swarm:general"
  "Significant-Gravitas/AutoGPT:general"
  "openclaw/openclaw:platform"
)

# Build JSON
echo '{"last_updated": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'", "frameworks": [' > "$DATA_FILE"

FIRST=true
TOTAL_STARS=0
MOST_POPULAR=""
MOST_STARS=0

for entry in "${FRAMEWORKS[@]}"; do
  repo="${entry%%:*}"
  category="${entry##*:}"
  
  echo "[$(date)] Fetching $repo..." | tee -a "$LOG_FILE"
  
  DATA=$(curl -s -H "Authorization: token $GITHUB_TOKEN" "https://api.github.com/repos/$repo")
  
  NAME=$(echo "$DATA" | jq -r '.full_name')
  if [ "$NAME" = "null" ]; then
    echo "[$(date)] WARNING: $repo not found or API error" | tee -a "$LOG_FILE"
    continue
  fi
  
  STARS=$(echo "$DATA" | jq -r '.stargazers_count')
  FORKS=$(echo "$DATA" | jq -r '.forks_count')
  ISSUES=$(echo "$DATA" | jq -r '.open_issues_count')
  UPDATED=$(echo "$DATA" | jq -r '.updated_at')
  LANGUAGE=$(echo "$DATA" | jq -r '.language')
  DESC=$(echo "$DATA" | jq -r '.description' | cut -c1-100)
  
  # Track stats
  TOTAL_STARS=$((TOTAL_STARS + STARS))
  if [ "$STARS" -gt "$MOST_STARS" ]; then
    MOST_STARS=$STARS
    MOST_POPULAR=$NAME
  fi
  
  # Write JSON entry
  if [ "$FIRST" = true ]; then
    FIRST=false
  else
    echo ',' >> "$DATA_FILE"
  fi
  
  jq -n \
    --arg name "$NAME" \
    --arg category "$category" \
    --argjson stars "$STARS" \
    --argjson forks "$FORKS" \
    --argjson issues "$ISSUES" \
    --arg updated "$UPDATED" \
    --arg language "$LANGUAGE" \
    --arg desc "$DESC" \
    '{name: $name, category: $category, stars: $stars, forks: $forks, issues: $issues, updated_at: $updated, language: $language, description: $desc, active: true}' \
    >> "$DATA_FILE"
  
  echo "[$(date)] $repo: $STARS stars, $FORKS forks" | tee -a "$LOG_FILE"
done

# Close JSON
echo '], "summary": {"total_frameworks": '${#FRAMEWORKS[@]}', "total_stars": '$TOTAL_STARS', "most_popular": "'$MOST_POPULAR'", "fastest_growing": "aiming-lab/AutoResearchClaw"}}' >> "$DATA_FILE"

echo "[$(date)] Stats update complete. Total stars: $TOTAL_STARS" | tee -a "$LOG_FILE"

# Validate JSON
jq '.' "$DATA_FILE" > /dev/null || {
  echo "ERROR: Invalid JSON generated" | tee -a "$LOG_FILE"
  exit 1
}

echo "[$(date)] JSON validated successfully" | tee -a "$LOG_FILE"