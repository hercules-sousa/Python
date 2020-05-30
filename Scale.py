import random

def sortear_nota():
  valor = random.randint(0, len(notas) - 1)
  return notas[valor] 

def obter_escala(x, notas):
  esc = []
  for k in range(0, 5, 2):
    esc.append(notas[x + k])
  x += 5
  for k in range(0, 7, 2):
    esc.append(notas[x + k])
  x += 7
  esc.append(notas[x]) 
  return esc
  

notas = 'C C# D D# E F F# G G# A A# B'
notas = notas.split()
for i in range(len(notas)):
  notas.append(notas[i])

while True:
  print('Digite uma nota:')
  n = input()
  if n not in notas:
    print('Nota inválida\n')
  else:
    for j in range(len(notas)):
      if (notas[j] == n):
        pos = j
        break
    escala = obter_escala(pos, notas)
    print("Escala da nota {}:".format(n))
    print(*escala)
    print()
