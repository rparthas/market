import sys
import os

from setuptools import setup,find_packages
setup(name="market",
      version="0.3",
      url='https://github.com/srijan-stack/market',
      description="this is a market calculator",
      long_description="use this to market",
      author="srijan",
      packages=find_packages(include=['src']),
      install_requires=[])