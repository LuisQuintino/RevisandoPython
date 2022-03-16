#Luis Quintino - Programa que converte a temperatura através de uma função.
def conv (f):
  c = (f - 32) * 5 / 9
  return c

t = conv (70)
print(t, "Celsius")