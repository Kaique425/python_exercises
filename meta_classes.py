class Meta(type):
    def __new__(msc, nome, bases, namespace):
        if nome == 'A':
            return type.__new__(msc, nome, bases, namespace)

        """"  Garante que um metodo seja implementado 
        em uma classe.
            
        if 'fala_oi' not in namespace:
            print('O metodo fala_oi deve ser implementado.')
        else:
            if not callable(namespace['fala_oi']):
                print(f'fala_oi precisa ser um metodo.')
        print(f"{nome} >> {namespace}") 
                                        """
        """ Garante que um determinado atributo não seja sobrescrevido. """
        if 'attr_class' in namespace:
            print(f'{nome} tentou sobrescrever o attr_classe')
            del namespace['attr_class']

        return type.__new__(msc, nome, bases, namespace)


class A(metaclass=Meta):
    attr_class = 'Class A'


class B(A):
    attr_class = 'Class B'


class C(A):
    attr_class = 'Class C'


b = B()


print(b.attr_class)
