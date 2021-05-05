# Exercicio 1
"""
A = [1, 0, 5, -2, -5, 7]
print(A)
B = A[0] + A[1] + A[5]
print(B)

for valor in A:
    print(valor)

"""
# Exercicio 2
"""
vetor = []
for i in range(1, 7):
    num = float(input(f'Digite o {i}/6 elemento: '))
    vetor.append(num)
print(vetor)
"""
# Exercicio 3
"""
vetor1 = []
vetor2 = []

for i in range(1, 10 + 1):
    valor = float(input(f'Digite o número {i}/10: '))
    vetor1.append(valor)
    quad_valor = valor ** 2
    vetor2.append(quad_valor)
print(vetor1)
print(vetor2)
"""
# Exercicio 4
"""
vetor = []

while len(vetor) < 8:
    elemento = int(input(f'Digite o elemento de posição {len(vetor)} do vetor: '))
    vetor.append(elemento)

print(vetor)
posx = int(input('Digite a primeira posição do elemento desejado: '))

while posx < 0 or posx > 7:
    posx = int(input('Valor inválido! Digite entre 0 e 7: '))

posy = int(input('Digite a segunda posição do elemento desejado: '))

while posy < 0 or posy > 7:
    posy = int(input('Valor inválido! Digite entre 0 e 7: '))

x = vetor[posx]
y = vetor[posy]

soma = x + y

print(f'A soma do valor na posição {posx} com o valor da posição {posy} é: {soma}')
"""
# Exercicio 5
"""
lista = []
while len(lista) < 10:
    elemento = int(input(f'Digite o elemento na posição {len(lista)}: '))
    lista.append(elemento)

contador = 0
for numero in lista:
    if numero % 2 == 0:
        contador += 1
print(f'Em uma lista de {len(lista)} elementos, temos {contador} números pares')
"""
# Exercicio 6
"""
vetor = []
for i in range(0, 10):
    valor = int(input(f'Digite o valor na posição {i} do vetor: '))
    vetor.append(valor)
print(vetor)

valor_max = max(vetor)
valor_min = min(vetor)

print(f'O valor máximo é {valor_max} e o valor mínimo é {valor_min}')
"""
# Exercicio 7
"""
vetor = []

while len(vetor) < 4:
    elemento = int(input(f'Digite o valor do elemento na posição {len(vetor)}: '))
    vetor.append(elemento)
print(vetor)

print(f' O valor máximo é {max(vetor)} e se encontra na posição {vetor.index(max(vetor))}.')
"""
# Exercicio 8
"""
vetor = []

for i in range(0, 6):
    elemento = int(input(f'Digite o valor do elemento na posição {i}: '))
    vetor.append(elemento)

print(f'O Vetor é: {vetor}, ele invertido fica: {vetor[::-1]}')

"""


