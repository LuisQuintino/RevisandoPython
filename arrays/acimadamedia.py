#Luis Quintino - Programa para calculas as notas acima da média.
notas=[]
media =0
acima=[]
for i in range(10):
  notas.append(float(input("nota: ")))
media=sum(nota)/10
for i in notas:
  if i>media:
    acima.append(i)
print("notas acima da média: ", len(acima))