import Image

__author__ = 'daniel'


def cropJPG(box, img, out):
    image = Image.open(img)

    image_crop = image.crop(box)
    image_crop.save(out)

    del image, image_crop


def cropRw(box, img):
    size = (475, 220)
    image = Image.open(img)
    # new_image = image
    white_block = Image.new("RGB", size, "white")

    image_crop = image.crop(box)
    image_crop.save('tmp/testCrop.jpg')

    image.paste(white_block, (0, 90, 475, 310))
    image.paste(image_crop, (70, 90, 545, 300))

    image.save('tmp/testout2.jpg')

    del image, image_crop, white_block
