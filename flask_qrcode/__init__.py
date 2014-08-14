import datetime
import os.path
import random
import string
from uuid import uuid4

from flask import render_template, Blueprint, Markup, url_for

import qrcode as qrc

created_qrs = list() #created QRs information will be stored in memory so they are not re-created
correction_levels = {
    'L': qrc.constants.ERROR_CORRECT_L,
    'M': qrc.constants.ERROR_CORRECT_M,
    'Q': qrc.constants.ERROR_CORRECT_Q,
    'H': qrc.constants.ERROR_CORRECT_H
}

def search_created_qrs(filename, filedir, options):
    for qr in created_qrs:
        if options == qr['options'] and filedir == qr['filedir']:
            return created_qrs.index(qr)
    return None

def qrcode(data, filename=None, filedir='.', version=None, error_correction='L', box_size=10, border=0, fit=True, tag_id=None, tag_class=None, tag_title=None, tag_alt=None):
    #gets arguments by copying the current locals() and pops qrcode options related to future comparison
    current_options = locals().copy()
    [current_options.pop(e) for e in ['filename', 'filedir', 'tag_id', 'tag_alt', 'tag_title', 'tag_class']]

    create_file = bool
    qr_file = None
    # makes qr image using qrcode as qrc
    qr = qrc.QRCode(
        version=version,
        error_correction=correction_levels[error_correction],
        box_size=box_size,
        border=border
    )
    qr.add_data(data)
    qr.make(fit=fit)
    #checks if there's a created qr file with the same options in the same directory
    qr_index = search_created_qrs(filename, filedir, current_options)

    if filename is None and qr_index is not None:
        qr_file = created_qrs[qr_index]['filename']
        create_file = False
    elif filename is None and qr_index is None:
        suffix = str(uuid4())
        qr_file = '_'.join(["QRcode", suffix]) + '.png'
        create_file = True
    else:
        qr_file = filename + '.png'
        create_file = True

    qr_path = url_for('static', filename=os.path.join(filedir, qr_file))
    # creates a new file if needed
    if create_file:
        created_qrs.append({'options': current_options, 'filedir': filedir, 'filename': qr_file})
        try:
            with open('.' + qr_path, 'wb') as wb_file:
                qr_img = qr.make_image()
                qr_img.save(wb_file)
        except IOError as err:
            raise err()

    return Markup(render_template('qrcode/qrcode.html', qrcode_url=qr_path, tag_id=tag_id, tag_class=tag_class, tag_title=tag_title, tag_alt=tag_alt))


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
