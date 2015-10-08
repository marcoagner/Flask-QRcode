# coding=utf-8
import base64
from io import BytesIO

import qrcode as qrc
from flask import Blueprint

correction_levels = {
    'L': qrc.constants.ERROR_CORRECT_L,
    'M': qrc.constants.ERROR_CORRECT_M,
    'Q': qrc.constants.ERROR_CORRECT_Q,
    'H': qrc.constants.ERROR_CORRECT_H
}


def qrcode(data, version=None, error_correction='L', box_size=10, border=0, fit=True):
    """ makes qr image using qrcode as qrc See documentation for qrcode package for info"""
    qr = qrc.QRCode(
        version=version,
        error_correction=correction_levels[error_correction],
        box_size=box_size,
        border=border
    )
    qr.add_data(data)
    qr.make(fit=fit)

    # creates qrcode base64
    out = BytesIO()
    qr_img = qr.make_image()
    qr_img.save(out, 'PNG')

    return u"data:image/png;base64," + base64.b64encode(out.getvalue()).decode('ascii')


class QRcode(object):
    def __init__(self, app=None, **kwargs):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.register_blueprint(app)
        app.add_template_filter(qrcode)
        app.add_template_global(qrcode)

    def register_blueprint(self, app):
        module = Blueprint('qrcode',
                           __name__,
                           template_folder='templates')
        app.register_blueprint(module)
        return module
