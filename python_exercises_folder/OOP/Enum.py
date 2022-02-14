from enum import Enum, auto

""" Enum é muito utilizado quando se precisa escolher
    um conjunto de dados, tipos ou comandos. """


class Direction(Enum):
    """O 'auto' atribui automaticamente um valor aos campos."""

    right = auto()
    left = auto()
    up = auto()
    down = auto()


def move(direction):
    """Verificando se 'direction' é uma instancia da classe Direction"""
    if not isinstance(direction, Direction):
        raise ValueError("Can´t move to this direction!")

    return f" Move {direction.name}"


if __name__ == "__main__":
    print(move(Direction.right))
    print(move(Direction.left))
    print(move(Direction.up))
    print(move(Direction.down))
