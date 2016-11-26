# coding=utf-8
import os
from flask_qrcode import QRcode
from flask_qrcode.utils import PolygonImage

basedir = os.path.abspath(os.getcwd())
testdir = os.path.join(basedir, 'tests')


def test_load_online_icon_qrcode():
    qrcode = QRcode()
    old_qr = qrcode('Test Data')
    new_qr = qrcode('Test Data',
                    icon_img='https://avatars2.githubusercontent.com/u/5016303')
    assert "data:image/png;base64," in new_qr
    assert len(new_qr) > len(old_qr)


def test_load_local_icon_qrcode():
    qrcode = QRcode()
    old_qr = qrcode('Test Data')
    new_qr = qrcode('Test Data',
                    icon_img=os.path.join(testdir, 'icon.jpg'))
    assert "data:image/png;base64," in new_qr
    assert len(new_qr) > len(old_qr)


def test_image_factory_qrcode():
    qrcode = QRcode()
    old_qr = qrcode('Test Data')
    new_qr = qrcode('Test Data', image_factory=PolygonImage)
    assert "data:image/png;base64," in new_qr
    assert len(new_qr) > len(old_qr)
