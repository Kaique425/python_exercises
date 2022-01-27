class Eletronico:
    def __init__(self, nome):
        self.nome = nome
        self.ligado = False

    def ligar(self):
        if self.ligado:
            info = f'{self.nome} já está ligado'
            print(info)
            self.log_info(info)
            return
        self.ligado = True

    def desligar(self):
        if not self.ligado:
            info = f'{self.nome} já está desligado'
            print(info)
            self.log_info(info)
            return
        self.ligado = False
