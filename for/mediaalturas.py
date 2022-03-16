#Luis Quintino - Programa que calcula a média das 20 alturas fornecidas.
total = 0
for i in range(1, 21):
    altura = float(input("Digite a altura: "))
    total += altura
    media = round((total / 20), 2)

print("a média é", media )