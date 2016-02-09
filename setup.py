from setuptools import setup
import os

try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = open('README.md').read()

setup(name='geograpy',
      version='0.3.7',
      description='Extract countries, regions and cities from a URL or text',
      long_description=long_description,
      url='https://github.com/zcarwile/geograpy',
      author='Jonathon Morgan',
      author_email='jonathon@ushahidi.com',
      license='MIT',
      packages=['geograpy'],
      install_requires=[
            'numpy',
            'nltk',
            'jellyfish',
            'pycountry'
      ],
      scripts=['geograpy/bin/geograpy-nltk'],
      package_data = {
            'geograpy': ['data/*.csv'],
      },
      zip_safe=False)
