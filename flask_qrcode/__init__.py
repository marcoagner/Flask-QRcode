# -*- coding: utf-8 -*-
'''
 Copyright (C) 2016 Marco Agner

 This file is part of Flask-QRcode.

 Flask-QRcode is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 Flask-QRcode is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

'''
import io
import segno
from flask import Blueprint


class QRcode(object):
    """Generate QR Code image"""
    def __init__(self, app=None, config_jinja=True, **kwargs):
        self.app = app
        self._config_jinja = config_jinja

        if app:
            self.init_app(app)

    def __call__(self, *args, **kwargs):
        if self.app:
            return self.qrcode(
                static_dir=self.app.static_folder, *args, **kwargs)
        return self.qrcode(*args, **kwargs)

    def init_app(self, app):
        self.app = app
        self.register_blueprint(app)

        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['qrcode'] = self

        if self._config_jinja:
            self._qrcode = self.__call__
            app.add_template_filter(self._qrcode, 'qrcode')
            app.add_template_global(self._qrcode, 'qrcode')

    def register_blueprint(self, app):
        module = Blueprint('qrcode',
                           __name__,
                           template_folder='templates')
        app.register_blueprint(module)
        return module

    @classmethod
    def qrcode(cls, data, mode="base64", version=None, error_correction="L",
               box_size=10, border=0, fit=True, fill_color="black",
               back_color="white", **kwargs):
        """
        Makes qr image using qrcode as qrc. See documentation
        for qrcode package for info.

        :param data: String data.
        :param mode: Output mode, [base64|raw].
        :param version: The size of the QR Code (1-40).
        :param error_correction: The error correction used for the QR Code.
        :param box_size: How many pixels each "box" of the QR code.
        :param border: The number of box for border.
        :param fit: If `True`, find the best fit for the data.
        :param fill_color: Frontend color.
        :param back_color: Background color.

        :param icon_img: Small icon image name or url.
        :param factor: Resize for icon image (default: 4, one-fourth of QRCode)
        :param icon_box: Icon image position [left, top] (default: image center)
        """
        qr = segno.make_qr(data, version=version, error=error_correction,
                           boost_error=fit)
        if mode == 'base64':
            return qr.png_data_uri(scale=box_size, border=border,
                                   color=fill_color, background=back_color)
        elif mode == 'raw':
            out = io.BytesIO()
            qr.save(out, kind='png', scale=box_size, border=border,
                    color=fill_color, background=back_color)
