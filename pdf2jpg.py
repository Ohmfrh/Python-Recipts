import PythonMagick

__author__ = 'daniel'


def pdf2jpg(pdf):
    p = PythonMagick.Image()
    p.density('200')
    p.read(pdf)
    p.write('tmp/test1.jpg')


def pdf2jpgDHL(pdf):
    p = PythonMagick.Image()
    p.density('200')
    p.pread(pdf)
    p.write('tmp/dhlimg.jpg')
