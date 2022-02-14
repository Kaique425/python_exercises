
class A:
    def __init__(self, dados=[]):
        self.dados = dados
        print('Eu sou o INIT!!')

    def __del__(self):
        print("Objeto deletado.")

    def __call__(self):
        print("Foi chamado como uma função.")

    def __len__(self):
        l = 0
        lenght = [l + 1 for i in self.dados]
        return sum(lenght)

    def __str__(self):
        return 'Essa é a instancia da classe A'


a = A(dados=[1, 2, 3, 4, 5])
print(len(a))
a()
print(a)
for i in a.dados:
    print(i)
