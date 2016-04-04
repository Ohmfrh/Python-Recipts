from pdf2jpg import pdf2jpg
from cropReport import *
from mergeReport import mergeReport
from jpg2docx import jpg2docx
from directoryAccess import *
import time

__author__ = 'daniel'


def main():
    fedex()


if __name__ == "__main__":
    main()

def fedex():
    box1 = (0, 0, 736, 862)
    box2 = (750, 462, 1700, 1100)
    box3 = (0, 90, 505, 300)
    folder = 'guide/'
    i = 1.0
    total_files = 0
    current_time = time.strftime("%d_%m_%Y")

    files = getPDF(folder)

    total_files = len(files)

    for fil in files:
        doc_name = fil.split('.')
        pdf2jpg(os.path.join(folder, fil))
        cropJPG(box1, 'tmp/test1.jpg', 'tmp/testout1.jpg')
        cropJPG(box2, 'tmp/test1.jpg', 'tmp/testout2.jpg')
        cropRw(box3, 'tmp/testout2.jpg')
        mergeReport()
        jpg2docx('print/' + current_time + '_' + doc_name[0] + '.docx')
        cleanup()
        print repr((i/total_files)*100) + "%"
        i += 1
