__author__ = 'asafe'

from distutils.core import setup

setup(
    name='desafio-zoox',
    version='1.0',
    description='desafio',
    author='asafe',
    author_email='asafeao@if.uff.br',
    url='https://github.com/asafepy/desafio-zoox.git',
    packages=[
        'questoes',
        'crawler.core',
        'crawler.core.db',
        'crawler.core.modules',
        'crawler.core.utils',
        'crawler.config',
    ],
)
