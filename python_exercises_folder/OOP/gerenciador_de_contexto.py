import contextlib
from contextlib import contextmanager

"""class Abra:
    def __init__(self, arquivo, modo):
        print('Init da class executado.')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Entrou na __enter__')
        return self.arquivo

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('Saiu do __exit__')
        self.arquivo.close()
        # Não foi tratada a exceção
        return True """


@contextmanager
def arquivo(arquivo, modo):
    try:
        print('Abrindo arquivo...')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        arquivo.close()
        print('Fechando arquivo...')


with arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Teste 1 \n')
    arquivo.write('Teste 2 \n')
    arquivo.write('Teste 3 \n')

help(contextlib)
