"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o sotware precisa
ter permissão:
    - Permissão de Leitura -> Para ler o arquivo
    - Permissão de Escrita -> Para ler o arquivo

StringIO -> Utilizado para ler e criar arquivos em memória
"""

# Primeiro fazemos o import
from io import StringIO

mensagem = 'Esta é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio parai nserirmos o texto depois

arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')

# Agora tendo o arquivo, podemos utilizar tudo que já sabemos
print(arquivo.read())

arquivo.write('\nOutro Texto')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())
