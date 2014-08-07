from flask import render_template, Blueprint, Markup, url_for

import os.path

import qrcode as qrc

def qrcode(data, filename='QRcode', filedir='.', version=None, error_correction=qrc.constants.ERROR_CORRECT_L, box_size=10, border=0, fit=True):
    qr = qrc.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border
    )
    qr.add_data(data)
    qr.make(fit=fit)

    qrpath = url_for('static', filename=os.path.join(filedir, filename) + '.png' )

    with open('./' + qrpath, 'wb') as qrfile:
        qrimg = qr.make_image()
        qrimg.save(qrfile)

    return Markup(render_template('qrcode/qrcode.html', qrcode_url=qrpath))

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