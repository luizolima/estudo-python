"""
Seek e Cursors

seek() -> Utilizada para movimentar o cursor pelo arquivo.

arquivo = open('texto.txt', encoding='UTF-8')
print(arquivo.read())

# A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um
# parâmetro que indica onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com a função seek() -> Procurar
arquivo.seek(0)

print(arquivo.read())
arquivo.seek(22)

print(arquivo.read())

# readline() -> função que lê o arquivo linha a linha

print(arquivo.readline())  # Primeira linha

print(arquivo.readline())  # Segunda linha

print(arquivo.readline())  # Terceira linha

print(arquivo.readline())  # Quarta linha

print(arquivo.readline())  # Quinta linha

print(arquivo.readline())  # Sexta linha

print(arquivo.readline())  # Sétima linha

# readline() -> função que lê o arquivo linha a linha

ret = arquivo.readline()

print(type(ret))
print(ret)

print(ret.split(' '))

# readlines() -> transforma cada linha em um elemento de uma lista

linhas = arquivo.readlines()

print(len(linhas))

# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo
no disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar
os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo

1- Abrir o arquivo

2 - Trabalhar o arquivo

3 - Fechar o arquivo

# 1 - Abrir o arquivo
arquivo = open('texto.txt', encoding='UTF-8')

# 2 - Trabalhar o arquivo
print(arquivo.read())

print(arquivo.closed)  # False Verifica se o arquivo estã aberto ou fechado
# 3 - Fechar o arquivo
arquivo.close()

print(arquivo.closed)  # True Verifica se o arquivo estã aberto ou fechado

print(arquivo.read())

# OBS: Se tentarmos manipular o arquivo apõs seu fechamento, teremos um ValueError
"""

arquivo = open('texto.txt', encoding='UTF-8')

print(arquivo.read(50))
