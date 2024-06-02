# Registering new version

```
pip install build
python -m build --sdist --wheel

```

make sure that the `dist` directory contains `tar.gz` and `whl` files without specific python version.

```
twine upload --skip-existing dist/*
```