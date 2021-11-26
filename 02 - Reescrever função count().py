def quantidade(n, lista):
    qtd = 0
    for e in lista:
        if e == n:
            qtd += 1
    return qtd

n = 1
lista1 = []
while n != 0:    
    n = int(input('Insira um valor(Digite "0" para terminar): '))
    if n > 0:
        lista1.append(n)

numero = int(input('Qual número gostaria de saber a quantidade de vezes que aparece? '))
quant = quantidade(numero, lista1)

print(f'Sua lista: {lista1}')
print(f'Número solicitado: {numero}')
print(f'Quantidade de vezes que aparece: {quant}')


