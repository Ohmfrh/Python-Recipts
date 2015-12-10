from pdf2jpg import pdf2jpg
from cropJPG import cropJPG
from mergeReport import mergeReport

__author__ = 'daniel'

def main():
    pdf2jpg()
    cropJPG()
    mergeReport()

    print "DONE"


if __name__ == "__main__":
    main()