"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: http://pypi.org

colorama ->  É utilizado para permitier impressão de textos coloridos no terminal.

Instalando um módulo:

pip install nome_do_modulo

"""
# pip install colocarama

# Utilizando o pacote instalado
from colorama import init, Fore
init()

print(Fore.GREEN + 'Geek University')