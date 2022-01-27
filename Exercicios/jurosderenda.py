valor_inicial = int(input("Digite o valor:"))
anos_rendendo = int(input("Por quantos anos vocẽ deseja que seu dinheiro renda ? "))
count = 0
while anos_rendendo != 0:
    if count == 0:
        total = valor_inicial + (valor_inicial * 0.0415)   
    else:
        total = total * 1.0415
    anos_rendendo = anos_rendendo - 1
    count = count + 1
print(f'{total:.2f}')