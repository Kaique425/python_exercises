import csv

with open('modules_exercises/clientes.csv', 'r') as file:
    dados = [x for x in csv.DictReader(file)]


with open('modules_exercises/clientes2.csv', 'w') as file:
    escreve = csv.writer(
        file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )
    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [chaves[0],
         chaves[1],
         chaves[2],
         chaves[3]]
    )

    for dado in dados:
        escreve.writerow(
            [dado['Nome'],
             dado['Sobrenome'],
             dado['E-mail'],
             dado['Telefone']]
        )
