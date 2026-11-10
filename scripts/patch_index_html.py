# Python script to update index.html with Scampedia 300+, Auto-Update, Admin View, and Clean Language
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update navigation label for database if needed
html = re.sub(
    r'<a href="#scam-database" onclick="showView\(\'scam-database\'\)" class="hover:text-white transition" data-i18n="navDatabase">[^<]+</a>',
    r'<a href="#scam-database" onclick="showView(\'scam-database\')" class="hover:text-white transition" data-i18n="navDatabase">Scampedia (300+)</a>',
    html
)

# 2. Update the prominent button at bottom of section #scams
html = re.sub(
    r'View All 150\+ Scams in Database \(2016-2026\)',
    r'Explore World Scampedia (300+ Scams Database)',
    html
)

print("Step 1 & 2 completed.")
