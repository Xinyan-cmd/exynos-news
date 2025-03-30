fetch('https://api.github.com/repos/Sexynos990/exynos-news/commits?path=backups/&per_page=1')
  .then(response => response.json())
  .then(data => {
    const lastBackup = new Date(data[0].commit.committer.date);
    document.getElementById('last-backup').textContent = lastBackup.toLocaleString();
  })
  .catch(() => {
    document.getElementById('last-backup').textContent = 'unknown';
  });
