#Luis Quintino - Programa que fatora o número fornecido.
n = int(input("valor a ser fatorado "))
total = n
for i in range(2, n):
  total = i * total
print(total)