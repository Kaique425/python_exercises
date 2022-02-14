from dataclasses import dataclass

""" O decorador aceita muitos parametros link da doc: 
    https://docs.python.org/3/library/dataclasses.html """


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    """ O metodo post init é acionado depois do init padrão """

    def __post_init__(self):
        self.nome_completo = f"{self.nome} {self.sobrenome}"


pessoa = Pessoa("Kaique", "Mota")

print(pessoa)
print(pessoa.nome)
print(pessoa.sobrenome)
print(pessoa.nome_completo)
