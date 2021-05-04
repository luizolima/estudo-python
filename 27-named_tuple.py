"""
Módulo Collection - Named Tuple

 https://docs.python.org/3/library/collections.html#collections.namedtuple

# Recap Tupla
tupla = (1, 2, 3)
print(tupla[1])

Named Tuple -> São tupla, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros

"""

# Importanto

from collections import namedtuple

# Precisamos definit o nome e parâmetro

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')  # Parâmetros com espaços

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')  # Parâmetros com virgulas

# Forma 3 = Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])  # Parâmetros com listas (colchetes)

# Usando

ray = cachorro(idade=2, raca='Chow-chow', nome='Ray')

print(ray)

# Acessando os dados

# Forma 1

print(ray[0])  # idade
print(ray[1])  # raça
print(ray[2])  # nome

# Forma 2

print(ray.idade)  # idade
print(ray.raca)  # raça
print(ray.nome)  # nome

print(ray.index('Chow-chow'))

print(ray.count('Chow-chow'))
