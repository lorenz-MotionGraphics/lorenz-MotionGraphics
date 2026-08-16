import os
import sys
import datetime
import requests
import re

print("▶ Script started")

TOKEN = os.environ.get("GITHUB_TOKEN")
if not TOKEN:
    print("❌ GITHUB_TOKEN not found")
    sys.exit(1)

OWNER, REPO = os.environ["GITHUB_REPOSITORY"].split("/")
YEAR = datetime.datetime.now().year

print(f"▶ Repo: {OWNER}/{REPO}")
print(f"▶ Year: {YEAR}")

HEADERS = {"Authorization": f"Bearer {TOKEN}"}

def get_commits():
    counts = [0] * 12
    page = 1

    while True:
        url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
        r = requests.get(url, headers=HEADERS, params={"per_page": 100, "page": page})

        print(f"Fetching page {page}: {r.status_code}")

        if r.status_code != 200:
            print(r.text)
            break

        data = r.json()
        if not data:
            break

        for c in data:
            d = c["commit"]["author"]["date"]
            dt = datetime.datetime.fromisoformat(d.replace("Z", ""))
            if dt.year == YEAR:
                counts[dt.month - 1] += 1

        page += 1

    print("▶ Monthly counts:", counts)
    return counts

def update_readme(data):
    if not os.path.exists("README.md"):
        print("❌ README.md not found")
        sys.exit(1)

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    if "<!-- CONTRIBUTIONS_CHART_START -->" not in content:
        print("❌ Chart markers missing")
        sys.exit(1)

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

    print("README updated")

if __name__ == "__main__":
    data = get_commits()
    update_readme(data)
