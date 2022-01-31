from banco import Banco
from cliente import Cliente
from contas import Conta, ContaCorrente, ContaPoupança

""" Testando as classes... """


banco = Banco()
cliente_k = Cliente("Kaique", 20)
cliente_f = Cliente("Flavio", 42)
conta_poupança = ContaPoupança(1111, 908098890, 5000)
conta_corrente = ContaCorrente(2322, 989898983, 401)
cliente_k.inserir_conta(conta_poupança)
cliente_f.inserir_conta(conta_corrente)

banco.cadastrar_cliente(cliente_f)
banco.cadastrar_cliente(cliente_k)
banco.autenticar(cliente_k)
print("---------------------------------------")
banco.autenticar(cliente_f)
cliente_k.conta.sacar(4000)
cliente_f.conta.sacar(901)
