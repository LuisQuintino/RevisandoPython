#Luis Quintino - Programa que calcula o aumento salarial através de porcentagem.
sal = float(input("Sua renda> "))
por = float(input("Porcentagem do aumento> "))
aumento = sal * (por / 100)
print("Sua nova renda= ", sal + aumento)