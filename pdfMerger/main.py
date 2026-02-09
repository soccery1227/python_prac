import PyPDF2

pdfFiles = ["1.pdf", "2.pdf", "3.pdf"]
merger = PyPDF2.PdfMerger()

for file in pdfFiles:
    with open(file, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        merger.append(reader)

merger.write("merged.pdf")
