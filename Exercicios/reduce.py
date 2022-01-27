from functools import reduce

from dados import lista, pessoas, produto

print(produto)
nova_lista = reduce(lambda ac, i: i['preco'] + ac, produto, 0)

print(nova_lista)
print(round(nova_lista / len(produto)))
