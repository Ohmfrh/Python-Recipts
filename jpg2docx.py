from docx import Document
from docx.shared import Mm

__author__ = 'daniel'

def jpg2docx(doc_name, img, w):
    document = Document()
    sections = document.sections
    section = sections[0]

    section.page_width = Mm(80)
    section.page_height = Mm(297)
    section.top_margin = Mm(0)
    section.bottom_margin = Mm(0)
    section.left_margin = Mm(0)
    section.right_margin = Mm(0)

    document.add_picture(img, width=Mm(w))

    document.save(doc_name)