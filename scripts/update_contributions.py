import os
import datetime
import re
import requests

TOKEN = os.environ["GITHUB_TOKEN"]
OWNER = os.environ["GITHUB_REPOSITORY"].split("/")[0]
REPO = os.environ["GITHUB_REPOSITORY"].split("/")[1]

HEADERS = {"Authorization": f"Bearer {TOKEN}"}
YEAR = datetime.datetime.now().year

def get_commits_per_month():
    counts = [0] * 12
    page = 1

    while True:
        url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
        r = requests.get(url, headers=HEADERS, params={"per_page": 100, "page": page})

        if r.status_code != 200 or not r.json():
            break

        for c in r.json():
            date = c["commit"]["author"]["date"]
            dt = datetime.datetime.fromisoformat(date.replace("Z", ""))

            if dt.year == YEAR:
                counts[dt.month - 1] += 1

        page += 1

    return counts

def update_readme(data):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    chart = (
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
        f"<!-- CONTRIBUTIONS_CHART_START -->\n{chart}\n<!-- CONTRIBUTIONS_CHART_END -->",
        content,
        flags=re.S
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated)

if __name__ == "__main__":
    data = get_commits_per_month()
    update_readme(data)
