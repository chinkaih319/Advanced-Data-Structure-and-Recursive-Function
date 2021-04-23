"""
File: blur.py
Name: Justin Huang
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the pic to      be blurred
    :return: blurred pic
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            r = 0
            g = 0
            b = 0
            time = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    p_x = x + i
                    p_y = y + j
                    if 0 <= p_x < img.width:
                        if 0 <= p_y < img.height:
                            p = img.get_pixel(p_x, p_y)
                            r += p.red
                            g += p.green
                            b += p.blue
                            time += 1
            n_p = new_img.get_pixel(x, y)
            n_p.red = r/time
            n_p.green = g/time
            n_p.blue = b/time
    return new_img


def main():
    """
    This code with four for-loops is designed to make one picture blurred.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
