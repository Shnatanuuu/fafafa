import os #C:\Users\Shantanu\Desktop\eps_files\pdf
from PyPDF2 import PdfMerger

# 📁 Root folder (contains PDFs + subfolders with PDFs)
root_folder = r"C:\Users\Shantanu\Desktop\eps_files\pdf"   # CHANGE THIS

# 📄 Output merged PDF
output_pdf = "Epstein_Files.pdf"

merger = PdfMerger()

pdf_count = 0

# Walk through root folder and all subfolders
for root, dirs, files in os.walk(root_folder):
    for file in sorted(files):
        if file.lower().endswith(".pdf"):
            pdf_path = os.path.join(root, file)
            merger.append(pdf_path)
            pdf_count += 1
            print(f"Added: {pdf_path}")

# Write merged PDF
if pdf_count > 0:
    with open(output_pdf, "wb") as f:
        merger.write(f)
    print(f"\n✅ {pdf_count} PDFs merged into '{output_pdf}'")
else:
    print("⚠️ No PDF files found.")

merger.close()