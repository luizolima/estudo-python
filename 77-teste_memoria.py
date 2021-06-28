"""
Teste de Memoria com Generators

# Sequencia de Fibonacci
1, 1, 2, 3, 5, 8, 13...

# Teste 1 - lista
for n in fib_lista(100000):
    print(n)
"""
# Funcao usando listas 449Mb


def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


# Funcao usando geradores

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste 2 Geradores 3Mb
for n in fib_gen(100000):
    print(n)

