#Luis Quintino - Programa feito com o intuito de calcular os lados de um triângulo e verificar se é escaleno, isóceles, equilátero ou se não é um triângulo.
l1 = int(input("Primeiro lado: "))
l2 = int(input("Segundo lado: "))
l3 = int(input("Terceiro lado: "))
 
if l1+l2 <= l3:
  print ("não é um triangulo")
elif l1 != l2:
  print ("é um triangulo")
  print ("ele é escaleno")
elif l1 == l22:
  print ("é um triangulo")
  print ("ele é isóceles")
else:
  print ("é um triangulo")
  print ("ele é equilátero")