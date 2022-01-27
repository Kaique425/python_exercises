
class TesteError(Exception):
    pass


def testar():
    raise TesteError('Ta errado')


try:
    testar()

except TesteError as error:
    print(f'erro: {error}')
