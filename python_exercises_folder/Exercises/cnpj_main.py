import cnpj

cnpj_number = str(input("Type your cnpj:"))
if cnpj.validate_cnpj(cnpj_number):
    print(f'{cnpj_number} is valid')

else:
    print(f"{cnpj_number} isn't valid")
