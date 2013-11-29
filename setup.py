from setuptools import setup, find_packages

setup(name = 'django-emd',
      version = '0.1.0',
      description = 'Django models for prices from EMD',
      author = 'Joshua Blake',
      author_email = 'joshbblake@gmail.com',
      packages = find_packages(),
      scripts = ['load_prices.sh',],
      data_files = [('/tmp', ['bin/create_prices.sql'],
)
