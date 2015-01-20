import StringIO
import base64

from flask import render_template, Blueprint, Markup, url_for
import qrcode as qrc

correction_levels = {
    'L': qrc.constants.ERROR_CORRECT_L,
    'M': qrc.constants.ERROR_CORRECT_M,
    'Q': qrc.constants.ERROR_CORRECT_Q,
    'H': qrc.constants.ERROR_CORRECT_H
}

def qrcode(data, version=None, error_correction='L', box_size=10, border=0, fit=True):
    # makes qr image using qrcode as qrc
    qr = qrc.QRCode(
        version=version,
        error_correction=correction_levels[error_correction],
        box_size=box_size,
        border=border
    )
    qr.add_data(data)
    qr.make(fit=fit)

    # creates qrcode base64
    io = StringIO.StringIO()
    qr_img = qr.make_image()
    qr_img.save(io)

    return "data:image/png;base64," + base64.b64encode(io.getvalue())

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
