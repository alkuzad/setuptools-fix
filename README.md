This is example of https://github.com/pypa/setuptools/issues/1417 issue, and potential solution:

1. Create venv `python -mvenv tvenv` and source it (`call tvenv/Scripts/activate`)
1. install server requirements using `pip install -r requirements.txt`
2. Install patched setuptools (The only change is in `package_index.py` with `SETUPTOOLS_UNREDIRECTED_HEADER`):
   1. `cd setuptools`
   2. `python bootstrap.py`
   3. `pip install -e .`
   4. `cd ..`
3. run server in separate console `python src\test\server.py`
4. run `pip uninstall pip-tools`
5. run `python setup.py install` and see behaviour for pip-tools old installation. It will return 400.
6. set `SETUPTOOLS_UNREDIRECTED_HEADER` env variable to `true`, on win: `set SETUPTOOLS_UNREDIRECTED_HEADER=true`
7. run `python setup.py install` again, this will install pip-tools and fail on dependencies (not present here)

