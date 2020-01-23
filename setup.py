from setuptools import setup, find_packages
import os

path = os.path.abspath(os.path.dirname(__file__))


def read(filename):
    with open(os.path.join(path, filename), encoding='utf-8') as f:
        return f.read()


setup(
    name='emissions-api',
    author='Emissions API Developers',
    license='MIT',
    url='https://github.com/emissions-api/emissions-api',
    packages=find_packages(),
    install_requires=[
        'psycopg2',
        'connexion',
        'GeoAlchemy2',
        'geojson',
        'python-dateutil',
        'sentinel5dl',
        's5a',
        'SQLAlchemy',
    ],
    include_package_data=True,
    long_description=read('README.rst'),
    long_description_content_type='text/x-rst',
    entry_points={
        'console_scripts': [
            'emissionsapi-download=emissionsapi.download:download',
            'emissionsapi-preprocess=emissionsapi.preprocess:main',
            'emissionsapi-web=emissionsapi.web:entrypoint',
        ],
    },
)