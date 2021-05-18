"""
Trabalhando com Módulos Built-in (Módulos integrados, que já vem instalados no Python)
____________________________
| Python | Módulos built-in |
----------------------------

# Utilizando alias (apelidos) para módulos/funções

import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *  # Desse jeito, não precisa inserir, por exemplo = random.random(), apenas random()

print(random())

# Importando todo o módulo

import random

print(random.random())

# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())

https://docs.python.org/3/py-modindex.html

"""
# Costumamos utilizar tuple para colocar multiplos imports de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))
