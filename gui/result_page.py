import os
import tkinter as tk

from tkinter import messagebox, filedialog

from services.pdf_merger import merge_pdfs


class ResultPage:

    def __init__(self, pdf_files):

        self.window = tk.Toplevel()

        self.window.title("Search Results")

        self.window.geometry("750x500")

        self.pdf_files = pdf_files

        self.create_widgets()

    def merge_all_pdfs(self):

        output_file = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialfile="merged_output.pdf"
        )

        if not output_file:
            return

        success = merge_pdfs(self.pdf_files, output_file)

        if success:

            messagebox.showinfo(
                "Success",
                f"PDF files merged successfully!\n\nSaved to:\n{output_file}"
            )

        else:

            messagebox.showerror(
                "Merge Failed",
                "Failed to merge PDF files."
            )

    def create_widgets(self):

        title = tk.Label(
            self.window,
            text="PDF Search Results",
            font=("Segoe UI", 20, "bold")
        )

        title.pack(pady=(20, 5))

        count_label = tk.Label(
            self.window,
            text=f"✓ {len(self.pdf_files)} PDF files found",
            font=("Segoe UI", 11)
        )

        count_label.pack(pady=(0, 15))

        frame = tk.Frame(self.window)

        frame.pack(padx=20, pady=10, fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame)

        scrollbar.pack(side="right", fill="y")

        listbox = tk.Listbox(
            frame,
            width=75,
            height=10,
            font=("Segoe UI", 10),
            yscrollcommand=scrollbar.set
        )

        listbox.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=listbox.yview)

        for pdf in self.pdf_files:
            listbox.insert(tk.END, os.path.basename(pdf))

        merge_button = tk.Button(
            self.window,
            text="Merge PDFs",
            width=22,
            height=2,
            command=self.merge_all_pdfs
        )

        merge_button.pack(pady=(15,25))