# Exercicio 01
"""
qtd = int(input('Digite o números de iterações: '))
num = 0
for i in range(1, qtd +1):
    num += 3
    print(num)
"""
# Exercicio 02
"""
# Usando for
for x in range(3):
    for i in range(1, 101):
        print(i)
# Usando while
cont1 = 1
i = 1
while cont1 <= 3:
    while i <= 2:
        print(i)
        i += 1
    i = 1
    cont1 += 1
"""
# Exercicio 03
"""
num = 10
while num >= 0:
    print(num)
    num -= 1
print('FIM')
"""
# Exercicio 04
"""
x = int(input('Declare um número: '))

while x <= 100000: #  Usando While
    print(x)
    x = x + 1000
"""
# Exercicio 05
"""
qtd = int(input('Digite a quantidade de quantos primeiros números você deseja: '))
num = 0
soma = 0

for i in range(1, qtd + 1):
    num += 2
    soma += num
    print(num, end=' ')
print('')
print(f'A soma dos primeiros {qtd} números pares é: {soma}')
"""


