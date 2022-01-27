
carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 50))
carrinho.append(('Produto 3', 70))

total = sum([produto[1] for produto in carrinho])

print(total)
