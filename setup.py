from setuptools import setup, find_packages

setup(
    name='test',
    version='0.1.0',
    description='test',
    long_description='test',
    author='dawid@dawigoslawski.pl',
    author_email='dawid@dawidgoslawski.pl',
    url='http://localhost/',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    install_requires=['pip-tools']
)
