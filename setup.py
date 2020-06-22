from setuptools import setup

setup( name = 'lookup',
       version = '0.1',
       description = 'Terminal based dictionary/thesaurus',
       url = 'https://github.com/Enigmage/lookup.git',
       author = 'Ali Zaidi',
       author_email = 'alizaidi0786.az@gmail.com',
       license = 'GNU General Public License v2.0',
       packages = ['lookup'],
       install_requires = ['requests', 'bs4', 'colorama'],
       scripts = ['bin/pluck'],
       zip_safe = False 
        )
