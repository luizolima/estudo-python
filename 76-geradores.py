"""
Geradores
- Geradores (generators) são Iterators (Iteradores);

OBS: O Contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:
- Generators podem ser criados com funções geradores;
- funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)

--------------------------------------------------------------------------------------
/ Funções                            / Generator Functions                           /
--------------------------------------------------------------------------------------
/ Utilizam return                    / utilizam Yield                                /
--------------------------------------------------------------------------------------
/ retorna uma vez                    / podem utilizar yield múltiplas vezes          /
--------------------------------------------------------------------------------------
/ quando executada, retorna um valor / quanto executada, retorna um generator        /
--------------------------------------------------------------------------------------

print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(next(gen))  # 1

print('Geek')

for num in gen:
    print(num)


"""


# Exemplo Função Geradora (Generator Function)


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


# OBS: Uma Generator Function não é um generator. Ela gera um generator. OK?

gen = list(conta_ate(10))

print(gen)

