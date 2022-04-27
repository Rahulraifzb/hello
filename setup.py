from setuptools import setup,find_packages
import codecs
import os

here = os.path.abspath(os.path.disname(__file__))

with codes.open(os.path.join(here,"README.md"),encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name="Hello",
    packages=["Hello"],
    version="0.1",
    license="MIT",
    description="This is a very basic package which is used to return the hello",
    author="Rahul Rai",
    author_email="rrai06125@gmail.com",
    url="https://github.com/Rahulraifzb/hello.git",
    download_url="https://github.com/Rahulraifzb/hello.git",
    keywords=["hello","some","meaning"],
    install_require=[
        "django",
        "crispy_forms"
    ],
    classofiers=[
        "Development Status :: 1-Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operation System :: Microsoft :: Windows",
    ]
)