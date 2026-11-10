#!/usr/bin/env python3
"""
Updates openScamDetail to use centralized updateSeoMeta for dynamic SEO metadata management.
"""

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_snippet = '''      window.history.pushState(null, '', `#scam/${scam.slug}`);
      document.title = `${scam.name} - Scam Details & Red Flags | IsThisScamOrReal.com`;
      const metaDesc = document.getElementById('metaDescTag');
      if (metaDesc) metaDesc.setAttribute('content', `Learn how ${scam.name} works, 5 red flags, sample phishing text, and official helplines to stay safe.`);'''

new_snippet = '''      window.history.pushState(null, '', `#scam/${scam.slug}`);
      updateSeoMeta(
        `${scam.name} - Scam Details & Red Flags | IsThisScamOrReal.com`,
        `Learn how ${scam.name} works, 5 red flags, sample phishing text, and official helplines to stay safe.`,
        `scam/${scam.slug}`
      );'''

if old_snippet in text:
    text = text.replace(old_snippet, new_snippet)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully updated openScamDetail with updateSeoMeta!")
else:
    print("Warning: old_snippet exact match not found.")
