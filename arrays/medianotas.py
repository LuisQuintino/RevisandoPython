#Luis Quintino - Programa que calcula as médias das notas através de uma array.
notas=[]
media=0
for i in range(10):
  notas.append(float(input("nota: ")))
media=sum(notas)/10
media = round(media, 2)
print("media = ", media)