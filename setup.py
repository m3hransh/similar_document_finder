from setuptools import setup

setup(
    name='docsim',
    version='0.1',
    py_modules=['app'],
    install_requires=[
        'Click',
        'matplotlib',
        'google',
        'BeautifulSoup4',
        'request'
    ],
    entry_points='''
        [console_scripts]
        docsim=app:cli
    ''',
)