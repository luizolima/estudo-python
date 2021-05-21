"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrimos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivop é criado no sistema operacional

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrário teremos um TypeError

# Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado,
caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo
o conteúdo no arquivo anterior é perdido.

# Exemplo de escrita - modo 'w' - write (escrita)

# Forma tradicional de escrita em arquivo (não Pythônica)

arquivo = open('mais.txt', 'w', encoding='UTF-8')
arquivo.write('Um texto qualquer. \n')
arquivo.write('Mais um texto. \n')
arquivo.close()

# Forma Pythônica

with open('novo.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write('Novos dados em um arquivo é muito fácil. \n')
    arquivo.write('Outros colocar quantas linhas quisermos. \n')
    arquivo.write('Mais é a última linha. \n')

with open('Geek.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write('Geek ' * 1000)
"""

with open('frutas.txt', 'w', encoding='UTF-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break


