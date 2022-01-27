file = open('Teste.txt', 'w+')

file.write('Teste 1 2 3 4 5')

file.seek(0, 0)

print(file.read())
file.close()

with open('Teste2.txt', 'a+') as file:
    file.write('Teste 5 4 3 2 1')
