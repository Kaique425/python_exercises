from eletronico import Eletronico
from logmixin import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self.ligado:
            error = f'{self.nome} está desligado!'
            print(error)
            self.log_error(error)
            return

        if self._conectado:
            info = f'{self.nome} já esta conectado!'
            print(info)
            self.log_info(info)
            return
        print('Conectando...')
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            info = f'{self.nome} já está desconectado!'
            print(info)
            self.log_info(info)
            return
        self._conectado = False
