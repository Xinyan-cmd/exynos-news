import os
import json
import subprocess
from datetime import datetime, timezone
from bs4 import BeautifulSoup

IGNORE_FILES = ["test-post.html", "template.html"]
POSTS_DIR = "docs/news/current"
ARCHIVE_DIR = "docs/news/archived"

def get_creation_date(filepath):
    try:
        result = subprocess.run(
            ['git', 'log', '--diff-filter=A', '--format=%ad', '--date=short', '--', filepath],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip().split('\n')[-1]
    except:
        return datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d')

index = {
    "meta": {
        "schema": "3.0",
        "generated": datetime.now(timezone.utc).isoformat(),
        "archive_threshold_days": 180
    },
    "current": [],
    "archived": []
}

# Process current posts
for filename in os.listdir(POSTS_DIR):
    if filename in IGNORE_FILES or not filename.endswith('.html'):
        continue
    
    path = os.path.join(POSTS_DIR, filename)
    try:
        with open(path) as f:
            soup = BeautifulSoup(f, 'html.parser')
            
        title = soup.title.text.replace('| Exynos-News', '').strip() if soup.title else filename
        date_str = get_creation_date(path)
        
        index['current'].append({
            "path": filename,
            "title": title,
            "date": date_str
        })
    except Exception as e:
        print(f"⚠️ Error processing {filename}: {str(e)}")

# Process archived posts
for root, dirs, files in os.walk(ARCHIVE_DIR):
    for filename in files:
        if not filename.endswith('.html'):
            continue
        
        path = os.path.join(root, filename)
        year = root.split('/')[-2]
        quarter = root.split('/')[-1]
        
        index['archived'].append({
            "path": os.path.relpath(path, ARCHIVE_DIR),
            "year": year,
            "quarter": quarter,
            "date": get_creation_date(path)
        })

# Sort posts
index['current'].sort(key=lambda x: x['date'], reverse=True)
index['archived'].sort(key=lambda x: x['date'], reverse=True)

with open('docs/news/_index.json', 'w') as f:
    json.dump(index, f, indent=2)
