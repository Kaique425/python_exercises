import re

regressives_numbers = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def validate_cnpj(cnpj):
    cnpj = clean_cnpj(cnpj)
    if is_sequence(cnpj):
        return False
    try:
        new_cnpj = calculate_digit(cnpj=cnpj, cnpj_digit=1)
        new_cnpj = calculate_digit(cnpj=cnpj, cnpj_digit=2)

        if new_cnpj and new_cnpj == cnpj:
            return True
    except:
        return False


def clean_cnpj(cnpj):
    cnpj = re.sub(r'[^\w\s]', '', cnpj)
    return cnpj


def calculate_digit(cnpj, cnpj_digit):
    if cnpj_digit == 1:
        regressives = regressives_numbers[1:]
        cnpj = cnpj[:-2]
    elif cnpj_digit == 2:
        regressives = regressives_numbers
        cnpj = cnpj[:-1]
    else:
        regressives = []

    total = sum([int(cnpj[index]) * regress for index,
                 regress in enumerate(regressives)])

    digit = 11 - (total % 11)
    digit = digit if digit <= 9 else 0

    return f'{cnpj}{digit}'


def is_sequence(cnpj):
    sequence = cnpj[0] * len(cnpj)
    if sequence == cnpj:
        return True
    else:
        return False
