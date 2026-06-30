import os
import tkinter as tk
from tkinter import messagebox

from services.pdf_merger import merge_pdfs


class ResultPage:

    def __init__(self, pdf_files):

        self.window = tk.Toplevel()

        self.window.title("Search Results")

        self.window.geometry("700x450")

        self.pdf_files = pdf_files

        self.create_widgets()

    def merge_all_pdfs(self):

        output_file = "merged_output.pdf"

        merge_pdfs(self.pdf_files, output_file)

        messagebox.showinfo(
        "Success",
        "PDF files merged successfully!"
        )

    def create_widgets(self):

        title = tk.Label(
            self.window,
            text="PDF Search Results",
            font=("Arial", 18)
        )

        title.pack(pady=10)

        count_label = tk.Label(
            self.window,
            text=f"PDF Files Found: {len(self.pdf_files)}",
            font=("Arial", 12)
        )

        count_label.pack(pady=10)

        listbox = tk.Listbox(
            self.window,
            width=80,
            height=15
        )

        listbox.pack(pady=10)

        for pdf in self.pdf_files:
            listbox.insert(tk.END, os.path.basename(pdf))

        merge_button = tk.Button(
            self.window,
            text="Merge PDFs",
            width=20,
            command=self.merge_all_pdfs
        )

        merge_button.pack(pady=15)