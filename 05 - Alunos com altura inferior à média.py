nomes = []
idades = []
alturas = []
for e in range(30):
    n = input('Digite o nome do aluno: ')
    nomes.append(n)
    i = int(input('Digite a idade desse aluno: '))
    idades.append(i)
    a = float(input('Digite a altura desse aluno: '))
    alturas.append(a)
 
media = float((f'{sum(alturas) / len(alturas):.2f}'))

indice = -1
print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
for i in idades:
    indice += 1
    if i > 13:        
        if alturas[indice] < media:
            print(nomes[indice])




