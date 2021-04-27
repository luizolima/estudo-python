"""
Loop for

Loop -> Estrutura que se repete
For -> Um tipo de estrutura de repetição

C ou Java
for(int i = 0; i < 10; i++ ){
    //execução do loop
}

# Python
for item in iterável:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Listas
    Lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)

# Exemplos de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range)

range(valor_inicial, valor _final)

OBS: O valor final não é inclusivo

for numero in range(1, 10):
    print(numero)

Enumerate:

(0, seq[0]), (1, seq[1]), (2, seq[2]), ...

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Geek University'
for letra in nome:
    print(letra, end='')

Tabela de emoji Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""
# Original: U+1F60D
# Modificado: U0001F60D

emoji = 'U0001F60D '
for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D ' * num)
