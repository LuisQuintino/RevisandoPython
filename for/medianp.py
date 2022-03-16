"""Luis Quintino - Faça um algoritmo que:
• leia 20 números inteiros;
• escreva os números que são negativos;
• escreva a média dos números positivos."""

for i in range(-10, 10):
  if i > 0:
    pos += n
    somapos += 1
    mediaposi = round((pos / somapos), 2)
  elif i < 0:
    print(i)
print("média", mediaposi)