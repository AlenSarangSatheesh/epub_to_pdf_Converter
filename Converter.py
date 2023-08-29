import ebooklib
from ebooklib import epub
from reportlab.pdfgen import canvas

def convert_epub_to_pdf(epub_path, pdf_path):
    book = epub.read_epub(epub_path)

    pdf_canvas = canvas.Canvas(pdf_path)
    
    for item in book.get_items():
        if isinstance(item, ebooklib.epub.EpubHtml):
            content = item.content
            # Process the content (e.g., convert HTML to text)
            pdf_canvas.drawString(100, 700, content)
    
    pdf_canvas.save()

# Get input from user
epub_input = input("Enter the path to the EPUB file: ")
pdf_output = input("Enter the path for the output PDF file: ")

# Convert EPUB to PDF
convert_epub_to_pdf(epub_input, pdf_output)
