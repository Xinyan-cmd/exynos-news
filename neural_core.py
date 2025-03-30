import os
import json
import frontmatter
from bs4 import BeautifulSoup
from datetime import datetime

class RealityForge:
    def __init__(self):
        self.posts = []
        self.link_graph = {}

    def process_artifact(self, path):
        try:
            with open(path) as f:
                content = f.read()
            
            # Extract essence
            meta = self.extract_essence(path, content)
            self.posts.append(meta)
            
            # Repair reality
            self.fix_temporal_links(path, content)

        except Exception as e:
            print(f"Reality anomaly in {path}: {str(e)}")

    def extract_essence(self, path, content):
        meta = {
            'path': os.path.relpath(path, 'docs/news'),
            'title': 'Unknown',
            'date': datetime.now().isoformat(),
            'device': 'Unknown',
            'rom': 'Unknown'
        }

        # Parse frontmatter
        try:
            post = frontmatter.loads(content)
            meta.update(post.metadata)
        except:
            pass

        # HTML extraction
        soup = BeautifulSoup(content, 'html.parser')
        if soup.title:
            meta['title'] = soup.title.text.split('|')[0].strip()

        # Date extraction hierarchy
        date_sources = [
            lambda: meta.get('date'),
            lambda: soup.find('time').get('datetime'),
            lambda: datetime.fromtimestamp(os.path.getmtime(path)).isoformat()
        ]
        for source in date_sources:
            try: meta['date'] = source(); break
            except: continue

        return meta

    def fix_temporal_links(self, path, content):
        # Fix relative paths
        dir_depth = path.count('/') - 2
        prefix = '../' * dir_depth if dir_depth > 0 else './'
        
        # Rewrite links
        fixed = re.sub(
            r'(href|src)="(?!https?://)([^"]+)"',
            lambda m: f'{m.group(1)}="{prefix}{m.group(2)}"',
            content
        )
        
        with open(path, 'w') as f:
            f.write(fixed)

    def save_fabric(self):
        self.posts.sort(key=lambda x: x['date'], reverse=True)
        with open('docs/news/_index.json', 'w') as f:
            json.dump({
                'generated_at': datetime.now().isoformat(),
                'posts': self.posts
            }, f, indent=2)

# Initiate forge
fabric = RealityForge()
for root, _, files in os.walk('docs/news'):
    for file in files:
        if file.endswith('.html'):
            fabric.process_artifact(os.path.join(root, file))
fabric.save_fabric()
