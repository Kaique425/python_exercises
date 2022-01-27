def lista_de_clientes(clientes, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes)
    return lista


outra_lista = []
cliente1 = lista_de_clientes(['Fabricio', 'João', 'Carlos'], outra_lista)
cliente2 = lista_de_clientes(['Kaique', 'Kevin', 'Flavio'])

print(cliente1)
print(cliente2)
