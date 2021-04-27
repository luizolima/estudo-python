"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not
Operadores binários
    - and, or, is

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True.
Para o 'is', o valor é comparado com um segundo.

"""
ativo = False
logado = False

if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')

print(ativo is False)

