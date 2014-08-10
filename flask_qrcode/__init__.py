import os.path
import random
import string

from flask import render_template, Blueprint, Markup, url_for

import qrcode as qrc

createdQRs = {}

def qrcode(data, filename=None, filedir='.', version=None, error_correction=qrc.constants.ERROR_CORRECT_L, box_size=10, border=0, fit=True):
    currentQR = locals()
    createFile = bool
    qr = qrc.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border
    )
    qr.add_data(data)
    qr.make(fit=fit)

    try:
        pop_createdQR = createdQRs[data].copy()
        pop_createdQR.pop('filename')
        pop_currentQR = currentQR.copy()
        pop_currentQR.pop('filename')
    except:
        pass

    if filename == None and data in createdQRs and pop_createdQR == pop_currentQR and os.path.isfile('.' + url_for('static', filename=os.path.join(filedir, createdQRs[data]['filename']))):
        filename = createdQRs[data]['filename']
        createFile = False
    elif filename == None:
        suffix = ''.join([random.choice(string.ascii_letters + string.digits + '-_') for ch in range(12)])
        filename = 'QRcode_' + suffix + '.png'
        createFile = True
    else:
        filename = filename + '.png'
        createFile = True

    qrpath = url_for('static', filename=os.path.join(filedir, filename))

    if createFile is True:
        createdQRs[data] = currentQR
        createdQRs[data]['filename'] = filename

        try:
            with open('.' + qrpath, 'wb') as qrfile:
                qrimg = qr.make_image()
                qrimg.save(qrfile)
        except IOError as err:
            raise err("Could not create QR code file")

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