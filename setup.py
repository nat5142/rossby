import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='Rossby',
    version='0.1',
    author='Nicholas Tulli',
    author_email='nat5142@psu.edu',
    description='A wrapper for the U.S. National Weather Service API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    python_requires='-=3.7',
    install_requires=['requests>=2.20'],
    keywords='national weather service nws noaa api wrapper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS :: Independent'
    ]
)
