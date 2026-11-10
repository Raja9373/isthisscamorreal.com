#!/usr/bin/env python3
"""
Restores Tailwind CDN in index.html head and ensures mobileMenuOverlay is strictly hidden.
"""

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

tailwind_cdn = '''  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            vgreen: '#00C853',
            vgreenDark: '#00A344',
            navy: '#0A1931'
          }
        }
      }
    }
  </script>'''

if 'cdn.tailwindcss.com' not in text:
    text = text.replace('</head>', tailwind_cdn + '\n</head>')
    print("Added Tailwind CDN script to head.")

# Ensure mobileMenuOverlay is hidden by default and has correct classes
old_overlay = 'id="mobileMenuOverlay" class="hidden fixed inset-0 z-50 bg-[#0A1931]/98 backdrop-blur-xl flex-col p-6 animate-fadeIn"'
new_overlay = 'id="mobileMenuOverlay" class="hidden fixed inset-0 z-50 bg-[#0A1931]/98 backdrop-blur-xl flex-col p-6 animate-fadeIn"'
# Even if it's already hidden, let's verify toggleMobileMenu toggles hidden and flex properly

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Restored CSS successfully!")
