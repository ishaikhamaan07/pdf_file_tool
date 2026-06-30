from services.pdf_finder import find_pdfs
from services.pdf_merger import merge_pdfs

directory = r"C:\Users\Amaan\OneDrive\Desktop\sample cvs"

pdf_files = find_pdfs(directory)

print(pdf_files)

if pdf_files:
    merge_pdfs(pdf_files, "merged_output.pdf")
    print("Merge Complete")
else:
    print("No PDFs Found")