import Image

__author__ = 'daniel'


def cropJPG():
    box1 = (0, 0, 736, 862)
    box2 = (750, 462, 1700, 1100)
    filename = "img/test1.jpg"

    image = Image.open(filename)

    image_crop1 = image.crop(box1)
    image_crop2 = image.crop(box2)

    image_crop1.save('img/testout1.jpg')
    image_crop2.save('img/testout2.jpg')

    del image, image_crop1
