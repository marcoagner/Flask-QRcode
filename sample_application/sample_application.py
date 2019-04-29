# coding=utf-8
from flask import Flask, render_template, request, send_file

from flask_qrcode import QRcode


app = Flask(__name__)
qrcode = QRcode(app)


@app.route("/")
def index():
    return render_template("sample_application.html")


@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = request.args.get("data", "")
    return send_file(qrcode(data, mode="raw"), mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
