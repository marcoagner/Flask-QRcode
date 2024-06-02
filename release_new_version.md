# Registering new version

```
pip install build
python -m build --sdist --wheel

```

make sure that the `dist` directory contains `tar.gz` and `whl` files without specific python version.

```
twine upload --skip-existing dist/*
```
to do proper git tagging
```
git tag v<version>
git push
```

## updating docs

use python 3.8 or similar, it did not work with 3.11
```
pip install -e .
sphinx-build -M html docs docs/_build
```
