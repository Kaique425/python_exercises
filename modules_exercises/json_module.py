import json

from dados import clientes_json

produto = [
    {"nome": "Bola", "preco": 59.00},
    {"nome": "Lapis", "preco": 49.0},
    {"nome": "Caneta", "preco": 19.00},
    {"nome": "Borracha", "preco": 58.00},
    {"nome": "Caderno", "preco": 59.00},
    {"nome": "Tenis", "preco": 119.00},
    {"nome": "Mouse", "preco": 54.00},
    {"nome": "Tinta", "preco": 73.00},
    {"nome": "Pincel", "preco": 91.00},
    {"nome": "canivete", "preco": 19.00},
]

""" Dicionario para Json """
dados_json = json.dumps(produto)

print(type(dados_json))

""" String json para dicionario """
dados = json.loads(clientes_json)

print(type(dados))

with open("modules_exercises/clientes.json", "r") as file:
    text = json.load(file)
    print(text)
