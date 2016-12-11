# coding=utf-8
from flask import Flask, render_template, request, send_file

from flask_qrcode import QRcode
from flask_qrcode.utils import PolygonImage, BitmapImage


app = Flask(__name__)
app.add_template_global(PolygonImage, 'PolygonImage')
app.add_template_global(BitmapImage, 'BitmapImage')
qrcode = QRcode(app)


@app.route('/')
def index():
    return render_template('sample_application.html')


@app.route('/qrcode', methods=['GET'])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = request.args.get('data', '')
    return send_file(
        qrcode(data, mode='raw',
               box_size=20, border=1,
               back_color='transparent',
               image_factory=PolygonImage),
        mimetype='image/png'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
