class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print("Esta falando")


class Cliente(Pessoa):
    def __init__(self, nome, idade, tipo):
        super().__init__(nome, idade)
        self.tipo = tipo

    def comprar(self):
        print(f"{self.nome} está comprando...")


class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nome} está estudando...")


aluno = Aluno("Kaique", 20)
cliente = Cliente("Kauê", 19, "vip")

print(aluno.nome)
aluno.estudar()

print(cliente.nome)
print(cliente.tipo)
cliente.comprar()
