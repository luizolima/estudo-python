"""
Generator Expression

Em aulas anteriores nós estudamos:
 - List Comprehension;
 - Dicitonary Comprehension;
 - Set Comprehension;

 Não vimos:
 - Tuple Comprehension... porque elas se chaman Generators

 nomes = ['Carlos', 'Camila, 'Carla, 'Cassiano', 'Cristina', 'Vanessa']

 print(any([nome[0] == 'C' for nome in nomes])

 # Poderíamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Qual é a utilidade de getsizeof()? -> Retorna a quantidade de bytes em meméria do elemento passado como parâmetro
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memória. QUanto maior a string, mais espaço
print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(92345668823))

print(getsizeof(True))

from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof((x * 10 for x in range(1000)))

print(list_comp)
print(set_comp)
print(dict_comp)
print(gen)
"""

# Posso iterar no Generator Expression: Sim

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)
