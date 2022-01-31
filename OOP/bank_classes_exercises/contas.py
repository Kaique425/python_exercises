import re
from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero_da_conta, saldo):
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor
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
    def __init__(self, agencia, numero_da_conta, saldo, limite=500):
        super().__init__(agencia, numero_da_conta, saldo)
        self.limite = 500

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
