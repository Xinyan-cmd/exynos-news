# 📌 News Post Creation Guide
# READ CAREFULLY OTHERWISE YOU ARE COOKED!
❗ Mandatory Rules

    Keep all _ and > symbols

    Always use <pre><code> for commands

    Warnings must start with !

    And never ever try to change something without reasons. Did you understood?

🆘 Need Help?

Create an issue @Sexynos990 - DO NOT guess! 
UNLESS ITS SOMETHING STUPID.
## 1️⃣ Copy Template
```bash
/docs/news/current/TEMPLATE.html → Copy to /docs/news/current/[name of the news].html
# Example: NEWS-2025-03-28.html

## 2️⃣ Edit These Parts Only


<!-- REPLACE THESE LINES -->
<title>Your Title Here</title>

<header class="post-header">
  <h1>> Your Title Here_</h1>
  <p>For: [Device] | [ROM/Kernel]</p>
  <p>Published: YYYY-MM-DD</p>
</header>

<article class="post-content">
  <h2>> Installation_</h2>
  <pre><code>your_commands_here</code></pre>
  
  <h2>> Changelog_</h2>
  <ul>
    <li>Change 1</li>
    <li>Change 2</li>
  </ul>
  
  <h2>> Issues_</h2>
  <div class="warning">
    <p>! Important warning here</p>
  </div>
</article>

## 3️⃣ Never Touch Footer  outside of edit this page!!!!

<!-- LEAVE THIS EXACTLY AS IS -->
<footer class="post-footer">
  <p><a href="../index.html">Back to News Index</a>_</p>
  <p><a href="../../">Back to Home Terminal</a>_</p>
  <p>Contribute edits: 
    <a href="https://github.com/Sexynos990/exynos-news/edit/site-backup/docs/news/current/YOUR-FILENAME.html" target="_blank">
      Edit this page
    </a>
  </p>
</footer>
