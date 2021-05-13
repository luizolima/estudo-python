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
# Exercicio 5
"""
# Programa
raio = float(input('Digite o raio da esfera: '))
v = 4/3 * 3.14 * (raio ** 3)

print(f'O volume é: {v}')

# funçao

def volume_esfera(raio):
    v = 4/3 * 3.14 * (raio ** 3)
    return f'O volume é: {v}'

print(volume_esfera(3))

"""
# Exercicio 6
"""
def segundos(hora, minuto, segundo):
    total = hora * 3600 + minuto * 60 + segundo
    return f'O total é de {total} segundos'

print(segundos(1, 1, 0))
"""
# Exercicio 7
"""
def temp_conv_to_fahrenheit(temp_em_celsius):
    f = (temp_em_celsius * (9/5)) + 32
    return f'A temperatura de {temp_em_celsius} (Celisus) para Fahrenheit é {f}'


print(temp_conv_to_fahrenheit(100))
"""
# Exercicio 8
"""
def hipotenusa(cateto_a, cateto_b):
    h = (cateto_a ** 2 + cateto_b ** 2) ** 0.5
    return f'A hipotenusa é {h}'


print(hipotenusa(3, 4))
"""
# Exercicio 9
"""
def volume_cilindo(altura, raio):
    v_c = 3.14592 * (raio ** 2) * altura
    return f'O volume do cilindro é: {v_c}'


print(volume_cilindo(5, 5))
"""
# Exercicio 10
"""
def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    return num2


print(maior_numero(100, 50))
"""
# Exercicio 11
"""
def nota_final(nota1, nota2, nota3, *args):
    global nota
    if 'A' in args:
        nota = (nota1 + nota2 + nota3) / 3
        return f'A nota final é: {nota}'
    elif 'P' in args:
        nota = (nota1 * 5 + nota2 * 3 + nota3 * 2) / 10
        return f'A nota final é: {nota}'
    return f'Operação inválida'

print(nota_final(25, 50, 100, 'P'))
"""
# Exercicio 12


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

print(sum_digits(253))

# Exercicio 13
"""

def calculo(num1, num2, *args):
    if '+' in args:
        operacao = num1 + num2
        return f'A soma é: {operacao}'
    elif '-' in args:
        operacao = num1 - num2
        return f'A subtração é: {operacao}'
    elif '*' in args:
        operacao = num1 * num2
        return f'A multiplicação é: {operacao}'
    elif '/' in args:
        operacao = num1 / num2
        return f'A divisão é: {operacao}'
    return f'Operador Inválido'



print(calculo(50, 50, ''))

"""
# Exercicio 14

# Exercicio 16
"""
def pula_linha(qtd):
    print('=-' * qtd)


pula_linha(30)
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
