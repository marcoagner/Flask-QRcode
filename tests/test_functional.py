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
# coding=utf-8
import os
from flask_qrcode import QRcode

basedir = os.path.abspath(os.getcwd())
testdir = os.path.join(basedir, 'tests')


def test_load_online_icon_qrcode():
    qrcode = QRcode()
    old_qr = qrcode('Test Data')
    new_qr = qrcode('Test Data',
                    icon_img='https://www.agner.io/icon.jpg')
    assert "data:image/png;base64," in new_qr
    assert len(new_qr) > len(old_qr)


def test_load_local_icon_qrcode():
    qrcode = QRcode()
    old_qr = qrcode('Test Data')
    new_qr = qrcode('Test Data',
                    icon_img=os.path.join(testdir, 'icon.jpg'))
    assert "data:image/png;base64," in new_qr
    assert len(new_qr) > len(old_qr)
