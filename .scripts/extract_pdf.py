import sys
from pypdf import PdfReader

if len(sys.argv) < 2:
    print("Usage: python extract_pdf.py <pdf-path>")
    sys.exit(1)

path = sys.argv[1]
reader = PdfReader(path)
texts = []
for i, page in enumerate(reader.pages, start=1):
    try:
        t = page.extract_text()
    except Exception as e:
        t = None
    texts.append(f"--- Page {i} ---\n" + (t or "(no extractable text)") )
print("\n\n".join(texts))
