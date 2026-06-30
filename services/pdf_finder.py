import os

from utils.validators import validate_path


def find_pdfs(directory):
    """
    Search the given directory and all subdirectories for PDF files.
    """

    if not validate_path(directory):
        return []

    pdf_files = []

    for root, directories, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))

    return pdf_files