from random import randrange

lista = ['A', 'B', 'C']
mao = []

for i in range(len(lista)-1, -1, -1):
    numero_sorteado = randrange(i+1)
    mao.append(lista.pop(numero_sorteado-1))
print(mao)
