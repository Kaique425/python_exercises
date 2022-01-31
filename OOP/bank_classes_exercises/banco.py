class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []
        self.agencias = [1111, 2222, 3333]

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)
        self.contas.append(cliente.conta)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        print(cliente.conta.agencia)
        if cliente not in self.clientes:
            print("Cliente não esta em clientes")
            return False

        if cliente.conta not in self.contas:
            print("A conta não pertence ao nosso grupo de contas")
            return False

        if cliente.conta.agencia not in self.agencias:
            print("Agencia não pertence a nossas agencias")
            return False
        print("Autenticado")
        return True
