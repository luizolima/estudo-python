# Exercicio 1
"""
def numero_em_dobre(numero):
    return numero ** 2


print(numero_em_dobre(100))

"""
# Exercicio 2
"""
def data_atual(dia, mes, ano):
    return f'{dia} de {mes} de {ano}'


print(data_atual(20, 'dezembro', 1989))
"""
# Exercicio 3
"""
def positivo_negativo(numero):
    if numero < 0:
        return -1
    elif numero == 0:
        return 0
    return 1


print(positivo_negativo(50))
print(positivo_negativo(-50))
print(positivo_negativo(0))


"""
# Exercicio 4
"""
import math


def quadrado_perfeito(numero):
    if math.sqrt(numero).is_integer() is True:
        return f'{numero} é um quadrado perfeito'
    return f'{numero} não é um quadrado perfeito'


print(quadrado_perfeito(65))
"""

# Exercicio 22
"""
def exclamacao(numero):
    i = 1
    while i < numero:
        print('!' * i)
        i += 1
    return '!' * i


print(exclamacao(8))
"""

