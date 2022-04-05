from PIL import Image


def revers(message):
    img = Image.open('files/photos/file_0.jpg')
    rotated = img.rotate(180)
    rotated.save('file_0.jpg')
    img = Image.open('rotated_test.jpg')
    return img