from dados import lista, pessoas, produto

nova_lista = filter(lambda n: n['idade'] < 30, pessoas)

for n in nova_lista:
    print(n['nome'])
