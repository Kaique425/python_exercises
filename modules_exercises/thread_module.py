from threading import Lock, Thread
from time import sleep


class Ingresso:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print("-Não temos ingresso suficientes.")
            self.lock.release()
            return

        sleep(1)
        self.estoque -= quantidade
        print(
            f"-Você comprou {quantidade} de ingresso(s), restando {self.estoque} no estoque."
        )
        self.lock.release()


if __name__ == "__main__":
    ingresso = Ingresso(10)
    for i in range(1, 20):
        t = Thread(target=ingresso.comprar, args=(i,))
        t.start()
