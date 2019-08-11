import os.path
from setuptools import setup, find_packages

setup(
    name='photoshare',
    author='floatingeye',
    author_email='eriklougee@gmail.com',

    version='0.0.1',
    description='photo share app for cool pals',

    packages=find_packages(),
    install_requires=[
        'Flask==1.0.2',
        'requests==2.22.0',
        'py-bcrypt==0.4',
        'pymongo==3.8.0'
    ]
)
