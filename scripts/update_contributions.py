import requests
import datetime
import os
import re

TOKEN = os.environ["GITHUB_TOKEN"]
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

USERNAME = os.environ.get("GITHUB_REPOSITORY").split("/")[0]
YEAR = datetime.datetime.now().year

def get_commits_per_month():
    monthly = [0] * 12

    for month in range(1, 13):
        start = f"{YEAR}-{month:02d}-01T00:00:00Z"
        end_month = month + 1 if month < 12 else 1
        end_year = YEAR if month < 12 else YEAR + 1
        end = f"{end_year}-{end_month:02d}-01T00:00:00Z"

        url = (
            f"https://api.github.com/search/commits"
            f"?q=author:{USERNAME}+committer-date:{start}..{end}"
        )

        r = requests.get(url, headers={**HEADERS, "Accept": "application/vnd.github.cloak-preview"})
        if r.status_code == 200:
            monthly[month - 1] = r.json().get("total_count", 0)

    return monthly

def update_readme(data):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    new_chart = (
        "```mermaid\n"
        "xychart-beta\n"
        f"    title \"GitHub Contributions ({YEAR})\"\n"
        "    x-axis [\"Jan\",\"Feb\",\"Mar\",\"Apr\",\"May\",\"Jun\",\"Jul\",\"Aug\",\"Sep\",\"Oct\",\"Nov\",\"Dec\"]\n"
        "    y-axis \"Commits\" 0 --> 200\n"
        f"    line {data}\n"
        "```"
    )

    updated = re.sub(
        r"<!-- CONTRIBUTIONS_CHART_START -->.*?<!-- CONTRIBUTIONS_CHART_END -->",
        f"<!-- CONTRIBUTIONS_CHART_START -->\n{new_chart}\n<!-- CONTRIBUTIONS_CHART_END -->",
        content,
        flags=re.S
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated)

if __name__ == "__main__":
    commits = get_commits_per_month()
    update_readme(commits)
