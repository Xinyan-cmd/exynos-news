// Load archived content dynamically
document.querySelectorAll('.file-tree a').forEach(link => {
  link.addEventListener('click', async (e) => {
    e.preventDefault();
    const path = e.target.getAttribute('href');
    const viewer = document.getElementById('archive-viewer');
    
    try {
      const response = await fetch(`https://sexynos990.github.io/exynos-news/backups/${path}`);
      if (!response.ok) throw new Error('Archive not found');
      const html = await response.text();
      
      viewer.innerHTML = `
        <div class="archive-frame">
          ${html}
          <div class="archive-meta">
            > Archived from backups/${path}
            <br>> Last modified: ${new Date(response.headers.get('last-modified')).toLocaleDateString()}_
          </div>
        </div>
      `;
    } catch (error) {
      viewer.innerHTML = `
        <pre><code>ERROR: Failed to load archive.
        
Try accessing directly:
<a href="https://github.com/Sexynos990/exynos-news/tree/main/backups/${path}" target="_blank">/backups/${path}</a></code></pre>
      `;
    }
  });
});
