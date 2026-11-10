#!/usr/bin/env python3
"""
Updates OG and Twitter tags in index.html to absolute URLs using og-image.jpg
and updates vercel.json to serve og-image.jpg with correct content-type.
"""

import json

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_og_block = '''  <!-- Open Graph & Twitter Cards -->
  <meta property="og:site_name" content="IsThisScamOrReal.com" />
  <meta property="og:title" id="ogTitleTag" content="Is This a Scam? Free Scam Checker - Check Message, Link, Number, Email | IsThisScamOrReal.com" />
  <meta property="og:description" id="ogDescTag" content="Is this message a scam or real? Paste any SMS, WhatsApp message, link, number or email. Free scam checker gives instant answer in your language. No signup needed." />
  <meta property="og:url" id="ogUrlTag" content="https://isthisscamorreal.com/" />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="https://isthisscamorreal.com/favicon.svg" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" id="twTitleTag" content="Is This a Scam? Free Scam Checker - IsThisScamOrReal.com" />
  <meta name="twitter:description" id="twDescTag" content="Is this message a scam or real? Paste any SMS, WhatsApp message, link, number or email. Free scam checker gives instant answer in your language." />
  <meta name="twitter:image" content="https://isthisscamorreal.com/favicon.svg" />'''

new_og_block = '''  <!-- Open Graph & Twitter Cards -->
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

if old_og_block in html:
    html = html.replace(old_og_block, new_og_block)
    print("Replaced OG block in index.html.")
else:
    # Try regex or direct replacement of open graph section
    print("Warning: old_og_block exact match not found, checking alternatives...")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update vercel.json
with open('vercel.json', 'r', encoding='utf-8') as f:
    vcfg = json.load(f)

# Ensure header for og-image.jpg
headers = vcfg.get('headers', [])
og_header_exists = any(h.get('source') == '/og-image.jpg' for h in headers)
if not og_header_exists:
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
    print("Updated vercel.json with og-image.jpg header.")

print("OG image fix script completed successfully!")
