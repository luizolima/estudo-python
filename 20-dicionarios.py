"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}

print(type({}))

listas []
tuplas()
dicionários {}

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave' : 'valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados.

# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (menos comum)

paises = dict(br='Brasil', eua='Estados unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista;tupla


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises['br'])
print(paises['ru'])

# Forma 2 - Acessando via get - Recomendado

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe , teremos o erro KeyError

print(paises.get('br'))
print(paises.get('ru'))

pais = paises.get('py',)

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyE

if pais:
    print(f'Encontrei o país {pais}')
else:
    print("Não encontrei o país")

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada

pais = paises.get('py', 'Não Encontrado')
print(f'Encontrei o país {pais}')

# Podemos verificar se determinanda chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

    paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean) inclusive lista, tupla diciona'rio, como chaves
# de dicionarios.

# Tuplas por exemplo são bastate interessantes de serem utilizadas como chave de dicionários, pois as mesmas são
# imutáveis
localidade = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 71.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}
print(localidade)
print(type(localidade))


# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - mais comum

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado)  # receita.update{'Mai' : 500}

print(receita)

# Atualizando dados em um dicionario

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})
print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma
# CONCLUSÃO 2: Em dicionarios, NÃO podemos ter chaves repetidas

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1 - mais comum
ret = receita.pop('mar')
print(ret)
print(receita)

# OBS: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado
# OBS: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2

del receita['fev']
print(receita)

# Se a chave não existir será gerado um keyError
# Neste caso o valor removido não é retornado.

# Imagine que voce tem um comercio eletronico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de compras
    Produto 1:
        - nome:
        - quantidade:
        - preço
    Produto 2:
        - nome:
        - quantidade:
        - preço



# 1 - Poderiamos utilizar uma lista para isso? Sim

carrinho = []

produto1 = ['Playstation 4 ', 1, 2300.00]
produto2 = ['God of war 4', 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o índice de cada informação no produto.

# 2 - Poderiamos utilizar uma tupla para isso? Sim

produto1 = ('Playstation 4 ', 1, 2300.00)
produto2 = ('God of war 4', 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teriamos que saber qual é o índice de cada informação no produto.

# 3 - Poderiamos utilizar um dicionario para isso? Sim

carrinho = []

produto1 = {'Nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'Nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos facilmente produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação.

#Métodos de dicionários:

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))


# Limpar o dicionário

d.clear()
print(d)

Forma não usual de criação de dicionários

# forma 1 - Deep Copy

novo = d.copy()  # Deep Copy

print(novo)

novo['d'] = 4

print(d)
print(novo)

# forma 2 - Shallow Copy
novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

# forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

#OBS: O método fromkeys recebe dois parâmentros: um iterável e um valor
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado

veja = {}.fromkeys('teste','valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
"""

