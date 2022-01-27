from dados import lista, pessoas, produto


def aumenta_idade(p):
    p['idade'] = round(p['idade'] * 1.35, 2)
    return p


nome_pessoas = map(aumenta_idade, pessoas)

for p in nome_pessoas:
    print(p)
