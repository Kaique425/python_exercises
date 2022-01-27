from itertools import zip_longest
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

lista_soma = [n + n2 for n, n2 in zip_longest(lista_a,lista_b, fillvalue=0) ]

print(lista_soma)