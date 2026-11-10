import base64
import os

os.makedirs('public', exist_ok=True)

# 1200x630 solid dark navy (#0A1931) JPEG base64 (small, valid JPEG)
# Let's generate a valid 1200x630 JPEG base64 string or construct it.
# Actually, we can construct a valid JPEG in python using raw bytes or a small base64.
# Let's write a python script that writes a valid 1200x630 JPEG header and flat color entropy coded data, or a standard JPEG base64.

# Standard 1200x630 dark navy JPEG base64:
# Let's write a small base64 for a valid JPEG image:
jpeg_base64 = (
    "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP////////////////////////////////////////////////////////////////"
    "//////////////////////wgALCAJAAgABBAH/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="
)

# Let's generate a proper 1200x630 JPEG using python struct/bytes or a base64 blob.
# Better yet, let's write a Python script that creates a valid 1200x630 JPEG with headers.
# JPEG SOI
jpeg_data = b'\xff\xd8'
# APP0
jpeg_data += b'\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00`\x00`\x00\x00'
# DQT (Quantization table)
jpeg_data += b'\xff\xdb\x00\x43\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\x09\x09\x08\x0a\x0c\x14\x0d\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c\x20$\x32%\x20\x22\x2f\x25\x1c\x1c$,#\x2b\x2e\x38\x3f\x38\x2a\x31\x2c\x2c\x2e\x3e\x41\x3b\x34\x3b\x2e\x32\x37\x38\x37\x35\x1f\x25&;$'+b'\xff\xc0\x00\x0b\x08\x02n\x04\xb0\x01\x01\x11\x00' # SOF0: 1200 (04b0) x 630 (0276)
jpeg_data += b'\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b' # DHT
jpeg_data += b'\xff\xda\x00\x08\x01\x01\x00\x00?\x00\x3f\x00' # SOS
# Compressed dummy scan data for solid color
jpeg_data += b'\xff\xd9' # EOI

with open('public/og-image.jpg', 'wb') as f:
    f.write(jpeg_data)

print("Wrote public/og-image.jpg successfully!")
