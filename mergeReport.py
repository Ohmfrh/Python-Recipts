import Image

__author__ = 'daniel'


def mergeReport():
    size = width, height = 950, 1500
    area1 = (0, 0, 736, 862)
    area2 = (0, 862, 950, 638+862)

    image = Image.new("RGB", size, "white")

    slip1 = Image.open('img/testout1.jpg')
    slip2 = Image.open('img/testout2.jpg')

    image.paste(slip1, area1)
    image.paste(slip2, area2)

    image.save('img/report.jpg')

    del image, slip1, slip2