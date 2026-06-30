import tkinter as tk
from tkinter import filedialog

from services.pdf_finder import find_pdfs


class HomePage:

    def __init__(self):

        self.window = tk.Tk()

        self.window.title("PDF File Tool")

        self.window.geometry("700x250")

        self.directory = tk.StringVar()

        self.create_widgets()

        self.window.mainloop()

    def browse_directory(self):

        folder = filedialog.askdirectory()

        if folder:

            self.directory.set(folder)

    def search_pdfs(self):

        pdf_files = find_pdfs(self.directory.get())

        print(pdf_files)

    def create_widgets(self):

        title = tk.Label(
            self.window,
            text="PDF File Tool",
            font=("Arial", 20)
        )

        title.pack(pady=10)

        entry = tk.Entry(
            self.window,
            textvariable=self.directory,
            width=60
        )

        entry.pack(pady=10)

        browse_button = tk.Button(
            self.window,
            text="Browse",
            command=self.browse_directory
        )

        browse_button.pack()

        search_button = tk.Button(
            self.window,
            text="Search PDFs",
            width=20,
            command=self.search_pdfs
        )

        search_button.pack(pady=15)