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
        'core',
        'core.db',
        'core.modules',
        'core.utils',
        'config',
    ],
)
