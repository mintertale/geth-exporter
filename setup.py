#!/usr/bin/env python3

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(name='geth-exporter',
      version='2',
      description='go-Ethereum exporter for Prometheus',
      author='Alexandru Thomae',
      author_email='<alex@thom.ae> and <mintertale',
      scripts=['geth-exporter'],
      url='https://github.com/mintertale/geth-exporter',
      )
