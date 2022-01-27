""" Metaclasses são classes que criam classes..."""

A = type('A', (), {'attr': 'Olá mundo'})

a = A()

print(a)
print(a.attr)
