# coding=utf-8
from flask import Flask, render_template

from flask.ext.qrcode import QRcode

app = Flask(__name__)
QRcode(app)


@app.route('/')
def index():
    return render_template('sample_application.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
