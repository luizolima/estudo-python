"""
Pacotes

Módulo -> é apenas um arquivo Python que pode ter diversas funções para utilizarmos;

Pocote -> é um diretório contendo um coleção de módulos;

OBS: Nas versões 2.X do Python, um pacote Python deveria conter dentro dele um
arquivo chamado __init__.py

Nas versões do Python 3.X, não é mais obrigatório a utilização deste arquivo, mas normalmente ainda é utilizado para
manter compatibilidade

from geek import geek1, geek2

from geek.university import geek3, geek4

print(geek1.pi)

print(geek1.funcao1(4, 6))

print(geek2.curso)

print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())

"""

from geek.geek1 import funcao1
from geek.university.geek4 import funcao4

print(funcao1(1, 6))

print(funcao4())