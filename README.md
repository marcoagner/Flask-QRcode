Flask-QRcode
============
[![PyPI version](https://badge.fury.io/py/Flask-QRcode.svg)](https://badge.fury.io/py/Flask-QRcode)

> An elegant Flask extension to render QR codes using [python-qrcode](https://github.com/lincolnloop/python-qrcode)

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

It's awesome that you want to contribute to this package. Thanks!

The process is pretty straightforward...

1. Fork this repository
2. Checkout from master with to a feature branch with a name related to what is being contributed (e.g. "colored-qrcodes")
3. Install dependencies and flask_qrcode on editable mode
    ```
    pip install -e . # for installing flask_qrcode on editable mode (preferable)
    ```
4. Do your magic
5. Don't be shy and... Pull Request.
