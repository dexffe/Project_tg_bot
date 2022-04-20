from PIL import Image
import PIL.ImageOps
import numpy as np


def image_inversion(message):
    img = Image.open(message)

    rotated = img.rotate(270, expand=True)

    rotated.save('file_1.jpg')

    im = Image.open('file_1.jpg')

    return im


def image_invert(message):
    img = Image.open(message)

    inverted_image = PIL.ImageOps.invert(img)

    inverted_image.save('file_1.jpg')

    im = Image.open('file_1.jpg')

    return im


def image_blwht(message):
    img = Image.open(message)

    arr = np.asarray(img, dtype='uint8')
    k = np.array([[[0.2989, 0.587, 0.114]]])
    sums = np.round(np.sum(arr * k, axis=2)).astype(np.uint8)
    arr2 = np.repeat(sums, 3).reshape(arr.shape)
    img2 = Image.fromarray(arr2)

    img2.save('file_1.jpg')

    im = Image.open('file_1.jpg')

    return im