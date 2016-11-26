# coding: utf-8
#
# If you need to custom `box` for QR code. You need to implementing
# the `PilImage.drawrect` method.
# https://github.com/lincolnloop/python-qrcode/blob/master/qrcode/image/pil.py
# https://pillow.readthedocs.io/en/3.4.x/reference/ImageDraw.html
#

from __future__ import division
from qrcode.image.pil import PilImage
from PIL import Image
import math
import random
import os


sin = lambda x: math.sin(math.radians(x))
cos = lambda x: math.cos(math.radians(x))
tan = lambda x: math.tan(math.radians(x))


class CircleImage(PilImage):

    def drawrect(self, row, col):
        box = self.pixel_box(row, col)
        self._idr.ellipse(box, fill=self.fill_color)


class PolygonImage(PilImage):

    def pixel_poly(self, row, col):
        x = (col + self.border) * self.box_size
        y = (row + self.border) * self.box_size
        r = self.box_size / 2

        x1 = r * sin(72)
        y1 = r * cos(72)
        x2 = r * cos(54)
        y2 = r * sin(54)

        return [(x, r - y1 + y),
                (x1 + x, y),
                (x1 * 2 + x, r - y1 + y),
                (x1 + x2 + x, r + y2 + y),
                (x1 - x2 + x, r + y2 + y)]

    def drawrect(self, row, col):
        box = self.pixel_box(row, col)
        poly = self.pixel_poly(row, col)
        key = random.choice([0, 1, 2])
        if key == 0:
            self._idr.ellipse(box, fill=self.fill_color)
        elif key == 1:
            self._idr.rectangle(box, fill='#289')
        elif key == 2:
            self._idr.polygon(poly, fill='#747')


class BitmapImage(PilImage):

    images = ['icon.jpg', 'icon.png']
    root = None

    def get_img(self):
        im = random.choice(self.images)

        if not self.root:
            # search file
            for root, dirs, files in os.walk('.'):
                if im in files:
                    self.root = root

        return Image.open(os.path.join(self.root, im))\
                    .convert('RGBA')\
                    .resize((self.box_size, self.box_size))

    def drawrect(self, row, col):
        box = self.pixel_box(row, col)
        #self._idr.bitmap(box[0], self.get_img(), fill=self.fill_color)
        self._img.paste(box=box[0], im=self.get_img())
