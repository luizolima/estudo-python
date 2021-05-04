"""
Módulo Colletions - Deque

https://docs.python.org/3/library/collections.html#collections.deque

Podemos dizer que o deque é uma lista de alta performance
"""
# importando

from collections import deque

deq = deque('Geek')

print(deq)

# Adicionanedo elementos no deque

deq.append('y')  # Adiciona no final
print(deq)

deq.appendleft('k')  # Adiciona no começo
print(deq)

# Removendo elementos no deque

print(deq.pop())  # Remove e retorna o último elemento

print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento

print(deq)
