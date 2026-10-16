# Registering new version

Update the `version` in `pyproject.toml`, then run the tests. Build both
distributions with `uv`:

```
uv build --sdist --wheel
```

Check that `dist` contains a source `.tar.gz` and a universal
`py3-none-any.whl` wheel. Push the version tag to publish both files to PyPI
through GitHub Actions:

```
$version = uv version --short
git tag "v$version"
git push origin "v$version"
```

Add a PyPI API token as the repository Actions secret `PYPI_API_TOKEN`. Use a
project-scoped token for `Flask-QRcode`; the publish workflow reads it when a
`v*` tag is pushed. Someone with PyPI project access must create the token.

Documentation builds run for pull requests. Pushes to `master` also publish
the generated HTML to GitHub Pages. Set the repository's Pages source to
**GitHub Actions** once to enable deployment.

## updating docs

To build the docs locally, use Python 3.8, sync the development dependencies,
then run:

```
uv sync --python 3.8 --group dev
uv run sphinx-build -M html docs docs/_build
```
