#!/usr/bin/env python3
"""
Updates index.html with exact OG and Twitter meta tags and verifies vercel.json.
"""

import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove any existing og:image, og:image:secure_url, og:image:type, og:image:width, og:image:height, og:image:alt, twitter:image tags
import re
html = re.sub(r'<meta property=\"og:image[^>]*>\s*', '', html)
html = re.sub(r'<meta name=\"twitter:image[^>]*>\s*', '', html)

# The new exact tags to insert inside <!-- Open Graph & Twitter Cards -->
exact_tags = '''  <!-- Open Graph & Twitter Cards -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.isthisscamorreal.com/">
  <meta property="og:title" content="Is This a Scam? Free Scam Checker - Check Message, Link, Number, Email">
  <meta property="og:description" content="Paste any SMS, WhatsApp message, link, or email. Get instant scam score, red flags and safe next steps. Free, no signup.">
  <meta property="og:image" content="https://www.isthisscamorreal.com/og-image.jpg">
  <meta property="og:image:secure_url" content="https://www.isthisscamorreal.com/og-image.jpg">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="IsThisScamOrReal - Free Scam Checker">
  <meta property="og:site_name" content="IsThisScamOrReal.com">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Is This a Scam? Free Scam Checker">
  <meta name="twitter:description" content="Paste any message and check if it's a scam or real. Free, instant.">
  <meta name="twitter:image" content="https://www.isthisscamorreal.com/og-image.jpg">'''

# Replace the Open Graph comment block or insert before </head>
og_comment_block = re.search(r'<!-- Open Graph & Twitter Cards -->.*?(?=<meta name=\"twitter:card\"|</head>)', html, re.DOTALL)
if og_comment_block:
    html = html.replace(og_comment_block.group(0), exact_tags)
else:
    html = html.replace('</head>', exact_tags + '\n</head>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with exact OG meta tags.")

# Update vercel.json
with open('vercel.json', 'r', encoding='utf-8') as f:
    vcfg = json.load(f)

# Ensure rewrite rule excludes files with extensions (.*\\..*)
# The rewrite is already "/((?!api/|.*\\..*).*)": "/index.html"
headers = vcfg.get('headers', [])
og_header = next((h for h in headers if h.get('source') == '/og-image.jpg'), None)
if not og_header:
    headers.append({
        "source": "/og-image.jpg",
        "headers": [
            {
                "key": "Content-Type",
                "value": "image/jpeg"
            }
        ]
    })
    vcfg['headers'] = headers
    with open('vercel.json', 'w', encoding='utf-8') as f:
        json.dump(vcfg, f, indent=2)
    print("Updated vercel.json headers for og-image.jpg.")
