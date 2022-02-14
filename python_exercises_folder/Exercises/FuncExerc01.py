from time import sleep

def contador(a,b,c):
    print(f"A contagem será de {a} até {b} de {c} passos ",flush=True)
    if a >= b:
        if c < 0:
            for n in range(a,b-1,c):
                sleep(0.5)
                print(n, end=" ",flush=True)
        else:
            for n in range(a,b-1,-c):
                sleep(0.5)
                print(n, end=" ",flush=True)
    elif a <= b  or c < 0:        
        for n in range(a,b+1,c):
            sleep(1)
            print(n, end=" ", flush=True)
a = int(input("Inicio: "))
b = int(input("Fim: "))
c = int(input("Passos: "))

contador(a,b,c)