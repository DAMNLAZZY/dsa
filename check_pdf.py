import pdfplumber

pdf_path = r"e:\dsa\2026-07-14 23-11-01.pdf"
with pdfplumber.open(pdf_path) as pdf:
    print(f"Number of pages: {len(pdf.pages)}")
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        print(f"\nPage {i+1}: width={page.width}, height={page.height}")
        print(f"  Has text: {bool(text)}")
        print(f"  Number of chars: {len(page.chars)}")
        print(f"  Number of images: {len(page.images)}")
        if text:
            print(f"  Text preview: {text[:200]}")
        # Try tables
        tables = page.extract_tables()
        if tables:
            print(f"  Tables found: {len(tables)}")
