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
[Examples folder](https://github.com/marcoagner/Flask-QRcode/tree/master/sample_application)
