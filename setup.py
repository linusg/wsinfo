from setuptools import setup
from wsinfo import __version__

with open("README.rst", "r") as f:
    long_description = f.read()

setup(name="wsinfo",
      packages=["wsinfo"],
      version=__version__,
      description="Python package for simply retrieving information about a specific website.",
      long_description=long_description,
      author="Linus Groh",
      license="MIT license",
      author_email="mail@linusgroh.de",
      url="https://github.com/linusg/wsinfo",
      download_url="https://pypi.python.org/pypi/wsinfo",
      keywords=["website", "http"],
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.1",
          "Programming Language :: Python :: 3.2",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Topic :: Internet",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Software Development :: Libraries",
          "Topic :: Software Development :: Libraries :: Python Modules"],
      )
