from pdf2image import convert_from_path
from docx import Document
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

PDF_PATH = r'assets/contrato.pdf'

pages = convert_from_path(PDF_PATH, 500)
doc = Document()

for page in pages:
    text = pytesseract.image_to_string(page, lang='por')
    doc.add_paragraph(text)
    doc.add_page_break()

doc.save(r'assets/contrato.docx')
