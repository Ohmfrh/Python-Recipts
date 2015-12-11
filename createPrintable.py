from pdf2jpg import pdf2jpg
from cropReport import cropJPG
from mergeReport import mergeReport
from jpg2docx import jpg2docx

__author__ = 'daniel'

def main():
    pdf2jpg()
    cropJPG()
    mergeReport()
    jpg2docx()

    print "DONE"


if __name__ == "__main__":
    main()