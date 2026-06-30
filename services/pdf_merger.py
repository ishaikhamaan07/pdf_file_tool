from PyPDF2 import PdfMerger


def merge_pdfs(pdf_files, output_file):
    """
    Merge multiple PDF files into a single PDF.
    """

    merger = PdfMerger()

    try:

        for pdf in pdf_files:
            merger.append(pdf)

        merger.write(output_file)

        return True

    except Exception as error:

        print(f"Merge Error: {error}")

        return False

    finally:

        merger.close()