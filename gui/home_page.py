import tkinter as tk
from tkinter import filedialog, messagebox

from gui.result_page import ResultPage
from services.pdf_finder import find_pdfs
from utils.messages import (
    INVALID_PATH,
    NO_PDF_FOUND,
    ONE_PDF_FOUND,
)


class HomePage:

    def __init__(self):

        self.window = tk.Tk()

        self.window.title("PDF File Tool")
        self.window.geometry("750x350")
        self.window.resizable(False, False)

        self.directory = tk.StringVar()

        self.create_widgets()

        self.window.mainloop()

    def browse_directory(self):

        folder = filedialog.askdirectory()

        if folder:
            self.directory.set(folder)

    def search_pdfs(self):

        directory = self.directory.get()

        if not directory:
            messagebox.showwarning(
                "Warning",
                INVALID_PATH
            )
            return

        pdf_files = find_pdfs(directory)

        if len(pdf_files) == 1:
            messagebox.showinfo(
                "One PDF Found",
                ONE_PDF_FOUND
            )
            return

        if not pdf_files:
            messagebox.showinfo(
                "No PDFs Found",
                NO_PDF_FOUND
            )
            return

        ResultPage(pdf_files)

    def create_widgets(self):

        title = tk.Label(
            self.window,
            text="PDF File Tool",
            font=("Segoe UI", 22, "bold")
        )

        title.pack(pady=(20, 5))

        subtitle = tk.Label(
            self.window,
            text="Merge multiple PDF files into one document",
            font=("Segoe UI", 10)
        )

        subtitle.pack(pady=(0, 20))

        folder_label = tk.Label(
            self.window,
            text="Folder Location",
            font=("Segoe UI", 10, "bold")
        )

        folder_label.pack()

        entry = tk.Entry(
            self.window,
            textvariable=self.directory,
            width=75,
            font=("Segoe UI", 10)
        )

        entry.pack(pady=10, ipady=4)

        browse_button = tk.Button(
            self.window,
            text="Browse Folder",
            width=22,
            height=2,
            command=self.browse_directory
        )

        browse_button.pack(pady=8)

        search_button = tk.Button(
            self.window,
            text="Search PDFs",
            width=22,
            height=2,
            command=self.search_pdfs
        )

        search_button.pack(pady=10)

        status = tk.Label(
            self.window,
            text="Status: Ready",
            font=("Segoe UI", 9),
            fg="gray"
        )

        status.pack(side="bottom", pady=10)