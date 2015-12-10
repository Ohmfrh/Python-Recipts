import PythonMagick

__author__ = 'daniel'


def pdf2jpg():
    pdf = 'pdf/1.pdf'
    p = PythonMagick.Image()
    p.density('200')
    p.read(pdf)
    p.write('img/test1.jpg')