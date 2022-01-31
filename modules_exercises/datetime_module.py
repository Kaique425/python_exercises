from calendar import mdays
from datetime import datetime, timedelta
from locale import LC_ALL, setlocale

""" Configura a localização 
    link da documentação: https://docs.python.org/3/library/datetime.html """

setlocale(LC_ALL, "pt_BR.utf-8")

""" Obitendo a data atual. """
data = datetime(
    2022,
    1,
    31,
    14,
    32,
)

""" Formatando e monstrando na tela """

print(data)
print(data.strftime("%d/%m/%Y %H:%M:%S"))

""" Recebendo o timestamp da data atual"""
data_timestamp = datetime.timestamp(data)

""" Recebendo e formatando um timestamp """
print(datetime.fromtimestamp(data_timestamp).strftime("%d/%m/%Y %H:%M:%S"))

data_strp = datetime.strptime("31/01/2022 14:40:00", "%d/%m/%Y %H:%M:%S")
print(data_strp)

"""" Somando tempo """
data_delta = data + timedelta(seconds=200 * 90)
print(data_delta)


"""" Obtendo a diferença entre duas datas. """
data1 = datetime.strptime("30/04/2022 14:40:00", "%d/%m/%Y %H:%M:%S")
data2 = datetime.strptime("22/03/2022 14:40:00", "%d/%m/%Y %H:%M:%S")

dif = data1 - data2
print(f"A diferença é de {dif.days} dias.")

data_pt = datetime.now()
mes_atual = int(data_pt.strftime("%m"))
formatação = data_pt.strftime("%A %d de %B de %Y")

print(formatação)

""" mdays uma lista com os ultimos numeros dos mêses, assim passando o 
    numero do mês atual, podemos saber quantos dias o mesmo tem """

print(mes_atual, mdays[mes_atual])
