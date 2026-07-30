import pdfplumber
import pytesseract

from pdf2image import convert_from_bytes
from docx import Document

# Change this if you installed Tesseract somewhere else
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_pdf(file):

    text = ""

    pdf_bytes = file.file.read()

    # Reset pointer
    file.file.seek(0)

    # ---------- Try normal extraction ----------

    with pdfplumber.open(file.file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    # ---------- OCR Fallback ----------

    if text.strip():

        return text

    print("No text layer detected. Running OCR...")

    images = convert_from_bytes(pdf_bytes)

    for image in images:

        text += pytesseract.image_to_string(image)

    return text


def extract_docx(file):

    document = Document(file.file)

    return "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
    )