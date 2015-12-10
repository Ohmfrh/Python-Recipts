import Image

__author__ = 'daniel'


def main():
    size = width, height = 950, 1500
    area1 = (0, 0, 736, 862)

    image = Image.new("RGB", size, "white")

    slip1 = Image.open('img/testout1.jpg')
    slip2 = Image.open('img/testout2.jpg')

    image.paste(slip1, area1)

    image.show()

    del image, slip1, slip2


if __name__ == "__main__":
    main()
