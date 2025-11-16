import os
from multiprocessing import Process
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk

from ..pdf_utils import pdf_page_to_image


class PDFViewer:
    """Simple Tkinter based viewer for displaying generated diagrams."""

    def __init__(self, pdf, size, dpi=150):
        self._pdf = pdf
        self._size = size
        self._dpi = dpi
        self._process = None

    def open_pdf(self):
        """Open the viewer in a separate process."""
        self._process = Process(
            target=self._show_pdf,
            args=(self._pdf, self._size, self._dpi),
            name="ControlBlockDiagramViewer",
            daemon=True,
        )
        self._process.start()

    def close_pdf(self):
        """Terminate the viewer process if it is still running."""
        if self._process is not None:
            self._process.terminate()
            self._process.join(timeout=1)
            self._process = None

    def show_pdf(self):
        """Display the PDF in the current process (blocking)."""
        self._show_pdf(self._pdf, self._size, self._dpi)

    @staticmethod
    def _show_pdf(pdf, size, dpi):
        """Render the first PDF page and display it within a scrollable Tkinter window."""
        root = tk.Tk()
        root.title(os.path.basename(pdf))
        width = max(200, int(size[0]))
        height = max(200, int(size[1]))
        root.geometry(f"{width}x{height}")

        container = ttk.Frame(root)
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container, highlightthickness=0)
        h_scroll = ttk.Scrollbar(container, orient="horizontal", command=canvas.xview)
        v_scroll = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        canvas.configure(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)

        canvas.grid(row=0, column=0, sticky="nsew")
        v_scroll.grid(row=0, column=1, sticky="ns")
        h_scroll.grid(row=1, column=0, sticky="ew")

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        image = pdf_page_to_image(pdf, dpi=dpi)
        tk_image = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, image=tk_image, anchor="nw")
        canvas.image = tk_image
        canvas.config(scrollregion=(0, 0, image.width, image.height))

        root.mainloop()
