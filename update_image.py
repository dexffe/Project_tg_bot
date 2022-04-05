from PIL import Image


def revers(message):
    img = Image.open(message)
    rotated = img.rotate(270)         # Баг. При повороте он обрезает фото
    rotated.save('file_1.jpg')
    img = Image.open('file_1.jpg')
    return img