import pdfplumber
import os

pdf_path = r"e:\dsa\New Doc 10-01-2025 21.18 (1).pdf"
output_dir = r"e:\dsa\unit12_pages"
os.makedirs(output_dir, exist_ok=True)

with pdfplumber.open(pdf_path) as pdf:
    print(f"Total pages: {len(pdf.pages)}")
    # Check first page for text
    text = pdf.pages[0].extract_text()
    if text and len(text.strip()) > 50:
        print("PDF has text. Extracting all text...")
        for i, page in enumerate(pdf.pages):
            page_text = page.extract_text()
            if page_text:
                print(f"\n--- Page {i+1} ---")
                print(page_text)
    else:
        print("PDF is likely scanned. Extracting images...")
        for i, page in enumerate(pdf.pages):
            img = page.to_image(resolution=150)
            img_path = os.path.join(output_dir, f"page_{i+1}.png")
            img.save(img_path)
            print(f"Saved {img_path}")
