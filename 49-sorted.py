"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort()
só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável

Como o próprio nome diz, sorted() serve para ordenar.

OBS: O Sorted, SEMPRE retorna uma Lista com os elementos do iterável ordenados

# Exemplo

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior

print(numeros)

numeros = [6, 1, 8, 2]
print(numeros)

print((sorted(numeros)))
# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True))  # Ordena do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachrros", "vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(usuarios)

# Ordenando pelo username - Ordem Alfab~etica
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))
"""

# Último exemplo



# Ordenada da menos para a mais tocada
print(sorted(musicas, key=lambda musica: musica["tocou"]))

# Ordenada da mais para a menos tocada
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))
