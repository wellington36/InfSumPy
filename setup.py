from setuptools import setup, find_packages

VERSION = '1.0.5'
DESCRIPTION = 'Approximate infinite sums with guaranteed error.'

# Setting up
setup(
    name="InfSumPy",
    version=VERSION,
    author="Wellington Silva",
    author_email="<wellington.71319@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    url="https://github.com/wellington36/InfSumPy",
    license='GPL-3.0',
    packages=find_packages(include=["infsumpy", "infsumpy.*"]),
    install_requires=['mpmath'],
    keywords=['python', 'sum', 'series', 'infinite-series', 'approximation', 'guaranted-sum']
)
