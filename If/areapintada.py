#Luis Quintino - Programa que calcula a necessidade de latas de tintas através da área a ser pintada.
metros = float(input("área a ser pintada em m2: "))
tinta = (metros / 3) / 18
if tinta % 1 != 0:
  latas = tinta + 1
  valor_lata = int(latas) * 80
print("Estou devendo R$", valor_lata,"e comprarei", int(latas),"latas")