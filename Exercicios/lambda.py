
Products = [['Product 1', 10], ['Product 2', 39],
            ['Product 3', 110], ['Product 5', 210]]

Products.sort(key=lambda item: item[1])

print(Products)
