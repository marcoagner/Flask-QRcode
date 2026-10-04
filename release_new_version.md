# Registering new version

Update the `version` in `pyproject.toml`, then run the tests. Build both
distributions with `uv`:

```
uv build --sdist --wheel
```

Check that `dist` contains a source `.tar.gz` and a universal
`py3-none-any.whl` wheel. Publish them to PyPI:

```
uv publish
```

Create and push a Git tag using the version from `pyproject.toml` (PowerShell):

```
$version = uv version --short
git tag "v$version"
git push origin "v$version"
```

## updating docs

Use Python 3.8 or similar; the docs build did not work with Python 3.11.
Sync the project and its development dependencies, then build the docs:

```
uv sync --python 3.8 --group dev
uv run sphinx-build -M html docs docs/_build
```

Manually copy the generated files to the `gh-pages` branch and push it to the remote.
