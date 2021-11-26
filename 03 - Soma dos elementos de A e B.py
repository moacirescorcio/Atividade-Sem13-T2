listaA = []
listaB = []
listaC = []

for a in range(20):
    a = int(input('Insira um valor para a Lista A: '))
    listaA.append(a)

for b in range (20):
    b =int(input('Insira um valor para a Lista B: '))
    listaB.append(b)

indice_A = 0
indice_B = 0

for c in range(20):    
    listaC.append(listaA[indice_A] + listaB[indice_B])
    indice_A += 1
    indice_B += 1

print(f'Lista A: {listaA}')
print(f'Lista B: {listaB}')
print(f'Lista C: {listaC}')
