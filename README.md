## FlatBuffer Schemas

|name|description|verifiable|
|----|-----------|----------|
|hs00|Histogram schema|Y|

## For developers

### Building the package
```
python setup.py sdist bdist_wheel
```

### Install the commit hooks (important)
There are commit hooks for Black and Flake8.

The commit hooks are handled using [pre-commit](https://pre-commit.com).

To install the hooks for this project run:
```
pre-commit install
```

To test the hooks run:
```
pre-commit run --all-files
```
This command can also be used to run the hooks manually.
