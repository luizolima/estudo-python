"""
Modos de abertura de arquivo

r -> Abre para leitura - Padrão
r -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista gera FileExistsError.
a -> Abre para escrita adicionando o conteúdo ao final do arquivo.
+ -> Abre para o modo de atualização: Leitura e Escrita. (temos o controle do Cursor)

# OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo
será adicionado sempre ao final do arquivo. Com o modo 'a' não controlamos o cursor.

https://docs.python.org/3/library/functions.html#open

# Exemplo 'x'
try:
    with open('university.txt', 'x', encoding='UTF-8') as arquivo:
        arquivo.write('Teste de contúdo 2. \n')
except FileExistsError:
    print('Arquivo já existe')

# Exemplo 'a'

with open('frutas.txt', 'a', encoding='UTF-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
"""

with open('outro.txt', 'a+') as arquivo:
    arquivo.write('No topo!\n')
    arquivo.write('Nova linha.\n')
    arquivo.write('Mais uma linha.\n')