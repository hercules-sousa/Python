import random

notas = 'A B C D E F G Am Bm Cm Dm Em Fm Gm'
notas = notas.split()

praticar = []

for i in range(5):
  praticar.append(notas[random.randint(0, len(notas))])
print(*praticar)