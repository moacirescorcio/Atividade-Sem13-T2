#LETRA A -------
def quantidade(lista):
    qtd = 0
    for e in lista:
        qtd += 1
    return qtd

#LETRA B --------
def inverter(lista):
    count = 0    
    lista_invertida = []
    indice = len(lista) - 1
    while indice >= 0:
        lista_invertida.append(lista[indice])
        indice -= 1
    return lista_invertida

#LETRA C ----------
def menor(lista):
    menor = lista[0]
    for e in lista:    
        if e < menor:
            menor = e
    return menor

#LETRA D ---------
def maior(lista):
    maior = lista[0]
    for e in lista:
        if e > maior:
            maior = e
    return maior

#LETRA E -----------
def somar(lista):
    soma = 0
    for e in lista:
        soma += e
    return soma



lista1 = []
n = 1
while n != 0:
    n = int(input('Insira um valor (Digite "0" para terminar): '))    
    if n > 0:
        lista1.append(n)

print(f'Sua lista: {lista1}')
print(f'Quatidade de números: {quantidade(lista1)}')
print(f'Lista invertida: {inverter(lista1)}')
print(f'Menor valor: {menor(lista1)}')
print(f'Maior valor: {maior(lista1)}')
print(f'Somatório dos valores: {somar(lista1)}')

















