Flask-QRcode
============
[![PyPI version](https://badge.fury.io/py/Flask-QRcode.svg)](https://badge.fury.io/py/Flask-QRcode)

> A concise Flask extension to easily render QR codes on Jinja2 templates using
[python-qrcode](https://github.com/lincolnloop/python-qrcode)

You can read the [full documentation here](https://marcoagner.github.io/Flask-QRcode/).

![](QRcode.png)

## Installation
    
```
pip install Flask-QRcode
```

## Usage:

### Extend the app:

```
from flask_qrcode import QRcode
# [...]
QRcode(app)
# [...]
```

### Then use it within your templates:

#### Basic usage:

    <img src="{{ qrcode(STRING_TO_ENCODE) }}">
    
### More examples:
For more examples, just run the sample application in this repository.

[Sample Application](https://github.com/marcoagner/Flask-QRcode/tree/master/sample_application)

## Contributing:

Thank you for considering contributing to this package.

As this is a simple package, the process is pretty straightforward...

1. Fork this repository
2. Checkout from master with to a feature branch with a name related to what is being contributed (e.g. "colored-qrcodes")

\**It's highly recommended that your contribution either creates a new **feature**, **fixes** something OR **refactors** the code and does not mix these (e.g. one PR fixing some existent feature and refactoring non-related code).*

3. Install dependencies and flask_qrcode on editable mode
    ```
    pip install -e .  # for installing flask_qrcode on editable mode
    ```
4. Do your magic
5. Provide new tests for your work and check that both this and the old ones
   are passing
6. Pull Request!

## Testing:

1. Install dependencies and flask_qrcode on editable mode
```
pip install -e .  # for installing flask_qrcode on editable mode
```
2. Run pytest
```
python setup.py test  # on package's root dir
```
