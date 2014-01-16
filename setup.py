from setuptools import setup, find_packages


with open('README.rst') as fp:
    long_description = fp.read()


setup(
    name='Goodreads API Client',
    version='0.1.2',

    description='A simple Python client library for the Goodreads API',
    long_description=long_description,

    author='Devin Sevilla',
    author_email='dasevilla@gmail.com',

    url='https://github.com/dasevilla/goodreads-python',
    download_url='https://github.com/dasevilla/goodreads-python/tarball/master',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],

    install_requires=[
    ],

    packages=find_packages(),

)
