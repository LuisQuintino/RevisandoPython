#Luis Quintino - Programa que calcula a hipotenusa através de uma função.

def hipo (co, ca):
  from math import sqrt
  h = sqrt(co ** 2 + ca ** 2)
  return h

catetos = hipo (10, 10)
print(catetos)