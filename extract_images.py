import pdfplumber
from PIL import Image
import os

pdf_path = r"e:\dsa\2026-07-14 23-11-01.pdf"
output_dir = r"e:\dsa\pdf_pages"
os.makedirs(output_dir, exist_ok=True)

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        img = page.to_image(resolution=200)
        img_path = os.path.join(output_dir, f"page_{i+1}.png")
        img.save(img_path)
        print(f"Saved page {i+1} to {img_path}")

print("Done!")
