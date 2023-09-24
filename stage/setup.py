from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Decoding various code and languages'
LONG_DESCRIPTION = 'A package that allows to decode code.'

# Setting up
setup(
    name="decode_things",
    version=VERSION,
    author="JustWait",
    author_email="<justwaitnano@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['math', 'random'],
    keywords=['python', 'decode', 'code', 'decoding', 'decode things', 'hex', 'bin'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
