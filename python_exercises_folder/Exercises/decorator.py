
def validar(function):

    def valida(x, y):
        if x < 0 or y < 0:
            raise ValueError('Os valores não podem ser negativos')
        x *= 2
        y *= 2
        return function(x, y)

    return valida


@validar
def soma(x, y):
    return x + y


print(soma(1, 2))
