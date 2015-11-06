# coding=utf-8
from flask_qrcode import qrcode


def test_create_qrcode():
    new_qr = qrcode('Test Data')
    assert "data:image/png;base64," in new_qr
