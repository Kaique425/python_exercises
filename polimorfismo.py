from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self, msg):
        pass


class B(A):
    # É necessario ser implementado
    def falar(self, msg):
        print(f'B está falando de {msg}')


class C(A):
    # É necessario ser implementado
    def falar(self, msg):
        print(f'C está falando de {msg}')


b = B()

c = C()

b.falar('futebol')
c.falar('Programação')
