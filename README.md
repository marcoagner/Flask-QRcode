Flask-QRcode
============

A simple Flask extension to render QR codes on the template using [python-qrcode](https://github.com/lincolnloop/python-qrcode)

![](QRcode.png)

##Installation
    
```
pip install Flask-QRcode
```

##Usage:

###Extend the app:

```
from flask.ext.qrcode import QRcode
# [...]
QRcode(app)
# [...]
```

###Then use it within your templates:

####Basic usage:

    <img src="{{ qrcode(STRING_TO_ENCODE) }}">
    
###More examples:
[Sample Application](https://github.com/marcoagner/Flask-QRcode/tree/master/sample_application)

##Contributing:

It's awesome that you want to contribute to this package. Thanks in advance!

The process is pretty stratighforward...

1. Fork this repository
2. Checkout from Master with a feature branch (prefer naming it related to what is being contributed)
3. Do your magic
  * Install the dependencies:
  ```
  pip install -r requirements.txt
  pip install -e . # for installing flask_qrcode on editable mode
  ```
4. Don't be shy and... Pull Request!
