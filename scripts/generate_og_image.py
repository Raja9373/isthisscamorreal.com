#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('public', exist_ok=True)

width, height = 1200, 630
image = Image.new('RGB', (width, height), color='#0A1931')
draw = ImageDraw.Draw(image)

# Draw decorative gradient / shapes
draw.rectangle([0, 0, width, height], fill='#0A1931')

# Draw accent glow / card box in center
draw.rounded_rectangle([60, 60, width-60, height-60], radius=32, fill='#12284C', outline='#00C853', width=3)

# Try loading a font, fallback to default if not available
try:
    font_title = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 58)
    font_sub = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 32)
    font_brand = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 28)
except:
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()
    font_brand = ImageFont.load_default()

# Shield / Badge Box
draw.rounded_rectangle([120, 120, 220, 220], radius=24, fill='#00C853')
# Draw shield symbol representation
draw.text((150, 140), "🛡️", fill="#FFFFFF")

# Text
draw.text((260, 130), "Is This a Scam or Real?", fill="#FFFFFF", font=font_title)
draw.text((260, 210), "Paste Message • Get Instant Answer • Free", fill="#00C853", font=font_sub)

# Bullet points box
draw.rounded_rectangle([120, 280, width-120, 470], radius=20, fill='#060D1A', outline='#ffffff22', width=1)

draw.text((160, 310), "✓ Instant Risk Score (0-100/100)", fill="#E2E8F0", font=font_sub)
draw.text((160, 360), "✓ Detected Red Flags Breakdown", fill="#E2E8F0", font=font_sub)
draw.text((160, 410), "✓ Golden 2-Hour Recovery Protocol", fill="#00C853", font=font_sub)

# Footer brand
draw.text((120, height - 100), "IsThisScamOrReal.com", fill="#94A3B8", font=font_brand)
draw.text((width - 320, height - 100), "Global Threat Intelligence", fill="#00C853", font=font_brand)

image.save('public/og-image.jpg', 'JPEG', quality=95)
print("Generated public/og-image.jpg successfully!")
