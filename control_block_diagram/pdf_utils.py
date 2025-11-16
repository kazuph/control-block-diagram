import fitz  # PyMuPDF
from PIL import Image


def pdf_page_to_image(pdf_path, dpi=300):
    """Render the first page of a PDF file into a PIL image."""
    document = fitz.open(pdf_path)
    try:
        page = document.load_page(0)
        zoom = dpi / 72.0
        matrix = fitz.Matrix(zoom, zoom)
        pixmap = page.get_pixmap(matrix=matrix, alpha=True)
        mode = "RGBA" if pixmap.alpha else "RGB"
        image = Image.frombytes(mode, (pixmap.width, pixmap.height), pixmap.samples)
        return image
    finally:
        document.close()


def save_pdf_as_image(pdf_path, target_path, image_format="png", dpi=300):
    """Render a PDF file and persist it using a Pillow-supported image format."""
    image_format = image_format.lower()
    image = pdf_page_to_image(pdf_path, dpi=dpi)
    if image_format in ("jpg", "jpeg"):
        image = image.convert("RGB")  # JPEG does not support alpha channel
    image.save(target_path, format=image_format.upper())
