import re
from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
        return self._nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade
        return self._idade


pessoa = Pessoa("Kaique", 20)


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, conta):
        self._conta = conta
        return self._conta

    def inserir_conta(self, conta):
        self.conta = conta
        return self.conta


cliente = Cliente("Kaique", 20)
"""print(cliente.nome)
print(cliente.idade)
print(cliente.conta)"""


class Conta(ABC):
    def __init__(self, agencia, numero_da_conta, saldo):
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self._saldo = saldo

    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def detalhes(self):
        print(
            f"Agencia: {self.agencia} \n"
            f"Numero da conta: {self.numero_da_conta} \n"
            f"Saldo: {self.saldo}"
        )
        self.detalhes()

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupança(Conta):
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            print(
                f"Você sacou {valor}, restando {self.saldo} como saldo atual da sua conta."
            )
            return self.saldo
        else:
            print(
                f"Saldo insuficiente! você tentou sacar {valor} mas seu saldo é de {self.saldo} sendo assim faltou {re.sub(r'^-', '', str(self.saldo - valor))}"
            )


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_da_conta, saldo, limite):
        super().__init__(agencia, numero_da_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        limite = self.limite
        limite_total = limite + self.saldo

        saldo = limite_total - valor
        if valor <= limite_total:
            if saldo >= 0:
                print(f"Você retirou {valor}, sendo R$ {saldo} seu saldo atual.")

            elif saldo < 0:
                print(f"você retirou {valor}, sua fatura será de {saldo}")

            self.saldo = saldo
            return self.saldo
        else:
            print(
                f"você tentou retirar {valor} excedendo o limite atual da conta em {int(re.sub(r'^-','', str(saldo)))}!"
            )


class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []
        self.agencias = ["0001", "0002", "0003"]

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        agencias = self.agencias
        agencia_cliente = cliente.conta.agencia
        print(cliente.conta.agencia)
        if cliente in self.clientes and agencia_cliente in agencias:
            print("Esse cliente não está autenticado")


conta_poupança = ContaCorrente("0005", "908098890", 500, 500)
cliente = Cliente("Kaique", 20)
cliente.inserir_conta(conta_poupança)
banco = Banco()
banco.cadastrar_cliente(cliente)
banco.autenticar(cliente)
