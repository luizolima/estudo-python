"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizar no seu sistema.

Em Python dividimos os métodos em dois grupos: Métodos de instância e
Métodos de Classe.

# Métodos de instância

# O Método dunder init __init__ é um método especial chamado de construtor e sua
função é construir um objeto a partir da classe

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

OBS: Os métodos/funções dunder em Python são chamado de métodos mágicos.

ATENÇÃO! Por mais que possamos criar nossas próprias funções utilizando dunder (underline no início e no fim)
não é aconselhado. Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento
dessas funções mágicas internas da linguagem. Então, evite ao máximo. De preferência nunca o faça.

# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por underline.

p1 = Produto('Playstation4', 'Video-Game', 2300)

print(p1.desconto(50))

print(Produto.desconto(p1, 40))  # self, desconto

user1 = Usuario('Luiz', 'Otávio', 'luiz.oflima@gmail.com', '552103')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '12345')

print(user1.nome_completo())

print(Usuario.nome_completo(user1))

print(user2.nome_completo())

nome = input('Informe o nome: ')
sobrenome = input('Informe o Sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Iforme a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere')
    exit(1)

print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografada: {user._Usuario__senha}')  # Acesso de forma errada

# Métodos de Classe


"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


