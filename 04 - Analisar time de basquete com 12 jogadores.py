nome = []
altura = []

for n in range(12):
    n = input()
    nome.append(n)
    a = float(input())
    altura.append(a)


indice_mais_alto = altura.index(max(altura))
media = sum(altura) / len(altura)




print('JOGADOR MAIS ALTO DO TIME')
print(nome[indice_mais_alto])
print(f'{altura[indice_mais_alto]:.2f}')
print('ALTURA MÉDIA DO TIME')
print(f'{media:.2f}')
print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')

indice = -1
for m in altura:
    indice += 1        
    if m > media:        
        print(nome[indice])
        print(f'{altura[indice]:.2f}')
        
        
