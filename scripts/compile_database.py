# Compile all 10 categories into public/scams-data.js
import sys
import re
import json

sys.path.insert(0, 'scripts')
from cat1_investment import cat1
from cat2_job import cat2
from cat3_phishing import cat3
from cat4_call import cat4
from cat5_romance import cat5
from cat6_shopping import cat6
from cat7_govt import cat7
from cat8_banking import cat8
from cat9_ransomware import cat9
from cat10_classic import cat10

all_cats = [
    ("investment-crypto", "Investment & Crypto", "🪙", cat1),
    ("job-employment", "Job & Employment", "💼", cat2),
    ("phishing-message", "Phishing / Message / Link", "📩", cat3),
    ("call-impersonation", "Call & Impersonation", "📞", cat4),
    ("romance-sextortion", "Romance & Sextortion", "💔", cat5),
    ("shopping-ecommerce", "Shopping & Online Store", "🛒", cat6),
    ("govt-lottery", "Govt & Lottery", "🏛️", cat7),
    ("banking-financial", "Financial / Banking", "🏦", cat8),
    ("tech-ransomware", "Ransomware / Malware / Tech", "💻", cat9),
    ("classic-tricks", "Classic / Confidence Tricks (Wikipedia)", "🎭", cat10),
]

def make_slug(name, year, seen_slugs):
    base = re.sub(r'[^a-zA-Z0-9]+', '-', name.lower()).strip('-')
    if year:
        base = f"{base}-{str(year).lower()}"
    slug = base
    counter = 1
    while slug in seen_slugs:
        slug = f"{base}-{counter}"
        counter += 1
    seen_slugs.add(slug)
    return slug

seen_slugs = set()
scams_list = []
categories_meta = []

for slug, cat_name, icon, cat_items in all_cats:
    categories_meta.append({
        "slug": slug,
        "name": cat_name,
        "icon": icon,
        "count": len(cat_items)
    })
    for item in cat_items:
        scam_slug = make_slug(item["name"], item.get("year", ""), seen_slugs)
        scams_list.append({
            "id": scam_slug,
            "slug": scam_slug,
            "icon": item.get("icon", icon),
            "name": item["name"],
            "year": item["year"],
            "isLatest": item.get("is_latest", False),
            "country": item["country"],
            "category": item["cat"],
            "categorySlug": slug,
            "categoryName": cat_name,
            "score": item["score"],
            "desc": item["desc"],
            "sampleMsg": item["sample"],
            "source": item["source"],
            "kaiseHotaHai": item["kaise"],
            "redFlags": item["flags"],
            "kyaKarein": item["actions"]
        })

print(f"Total compiled scams: {len(scams_list)}")

sources_list = [
    {"id": "all", "name": "All Sources"},
    {"id": "Wikipedia", "name": "Wikipedia"},
    {"id": "FBI IC3", "name": "FBI IC3 (USA)"},
    {"id": "FTC", "name": "FTC (USA)"},
    {"id": "Action Fraud", "name": "Action Fraud (UK)"},
    {"id": "I4C India", "name": "I4C / Cybercrime.gov.in"},
    {"id": "Scamwatch", "name": "Scamwatch (Australia)"},
    {"id": "Canadian Anti-Fraud Centre", "name": "Canadian Anti-Fraud"},
    {"id": "Interpol", "name": "Interpol / Europol"},
    {"id": "Google News", "name": "Google News (2026)"}
]

js_content = f"""// IS THIS SCAM OR REAL - ULTIMATE WORLD SCAM DATABASE FOR SCAMPEDIA
// 300+ Verified Scams from Wikipedia, FBI IC3, FTC, Action Fraud, I4C India, Scamwatch, CAFC, Interpol, Google News
// Sources: Wikipedia, FBI IC3, FTC, Action Fraud, I4C India, Scamwatch - For education only.

window.SCAMPEDIA_SOURCES = {json.dumps(sources_list, indent=2)};

window.SCAMPEDIA_CATEGORIES = {json.dumps(categories_meta, indent=2)};

window.GLOBAL_SCAMS_DATABASE = {json.dumps(scams_list, indent=2)};
"""

with open('public/scams-data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully written to public/scams-data.js ({len(js_content)} bytes)")
