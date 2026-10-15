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

Configure PyPI trusted publishing once for this repository: add
`publish.yml` as a trusted publisher with the `pypi` environment. The publish
workflow runs when a `v*` tag is pushed.

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
