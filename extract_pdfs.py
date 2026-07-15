import pdfplumber
import os

pdfs = [
    r"e:\dsa\2026-07-14 23-11-01.pdf",
    r"e:\dsa\_DSA_QB-Mock_Endsem_QB.xlsx - QB_MockIn.pdf",
    r"e:\dsa\_DSA_QB-Mock_Endsem_QB.xlsx - QB_MockEndsem.pdf",
]

for pdf_path in pdfs:
    print(f"\n{'='*80}")
    print(f"FILE: {os.path.basename(pdf_path)}")
    print(f"{'='*80}")
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                print(f"\n--- Page {i+1} ---")
                print(text)
