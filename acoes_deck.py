from random import randrange
from copy import deepcopy
from constantes import *
from time import sleep
from cartas import *

# Iniciando os Jogadores
j1 = 'Danilo'
j2 = 'André'

# A função abaixo é responsável por embaralhar as cartas para um jogador receber seu deck de cartas
def gerar_deck_jogador(deck, nome_jogador):
    deck_temp = deepcopy(deck)
    deck_jogador = []

    for i in range(len(deck_temp)-1, -1, -1):
        numero_sorteado = randrange(i+1)
        deck_jogador.append(deck_temp.pop(numero_sorteado-1))
    
    print("Entregando o deck embaralhado do jogador: "+nome_jogador+" \n")
    #sleep(2)
    return deck_jogador

#deck_jogador1 = GerarDeckJogador(deck, j1)
# print(deck_jogador1)

# A função GerarMãoInicial retira do deck 5 cartas para o jogador iniciar seu jogo
def gerar_mao_inicial(deck_jogador, n_cartas, nome_jogador):
    mao_inicial = deepcopy(deck_jogador[0:n_cartas])
    deck_jogador = deck_jogador[n_cartas:]
    #sleep(2)

    print('A mao inicial do jogador '+nome_jogador+' foi entregue!'+"\n")

    return [mao_inicial, deck_jogador]

'''
As duas linhas abaixo são responsáveis por receber o retorno da função GerarMãoInicial
e para printar a mensagem apenas uma vez, optei por criar uma variavel chamada "vetor_mao_inicial_e_deck_atual"
que é uma lista com os dois valores, depois atribuo esses valores para as variaveis de interesse
'''
#vetor_mao_inicial_e_deck_atual = GerarMãoInicial(deck_jogador1, N_CARTAS_INICIAL, j1)
#mao_inicial, deck_atual = vetor_mao_inicial_e_deck_atual[0], vetor_mao_inicial_e_deck_atual[1]

#print(deck_atual)

# A função abaixo mostra a mão atual de maneira mais amigável
def apresentar_mao_atual(mao_atual, nome_jogador):
    print(nome_jogador+', sua mao atual eh a seguinte:')
    print('')

    cont = 1
    for carta in mao_atual:
        if carta["Classe"] != FEITICO:
            print(str(cont)+'. '+carta['Nome']+' | Classe: '+carta['Classe']+' | ATK: '+str(carta['Ataque'])+' | VIDA: '+str(carta['Vida']))
        else:
            print(str(cont)+'. '+carta['Nome']+' | Classe: '+carta['Classe']+" | Ação: "+str(carta["Acao"]))
        #sleep(0.5)
        cont += 1

# A função Sacar retira uma carta do deck do jogador e põe essa mesma carta na sua mao atual
def Sacar(mao_atual, deck_atual, nome_jogador):
    carta = deepcopy(deck_atual[0])
    deck_atual = deck_atual[1:]
    mao_atual.append(carta)

    print('')
    input('O jogador: '+nome_jogador+' acaba de sacar uma carta do seu deck')
    print('')
    return [mao_atual, deck_atual]

def ReceberCartaEscolhida(mao_atual, nome_jogador):
    print()
    indice_carta = input(nome_jogador+", escolha o numero da carta a ser jogada"+"\n").strip()
    sleep(1)

    while True:
        if indice_carta not in INDICE_CARTA_POSSIVEL:
            indice_carta = input("Por gentileza, insira um numero valido"+"\n").strip()
        else:
            indice_carta = int(indice_carta)
            break
        
    carta_jogada = mao_atual.pop(indice_carta-1)
    print("Voce escolheu a carta: "+carta_jogada["Nome"])
    return carta_jogada

def escolher_general(generais):

    general_escolhidos = []
    input("Atualmente temos 5 generais por favor escolha um a seguir:""\n")
    print("Você pode escolher digitando o nome dele ou o seu numero.")
    #sleep(1)
    for i in range(len(deck_generais)):
        print(deck_generais[i]["Nome"], end=" " )
        print(f"e seu numero de escolha é {i+1} ")
        #sleep(1)
    for c in range(2):
        while True:
            entrada = input("Por favor, insira um nome ou numero válido:""\n").strip().lower()
            if entrada in NUMERO_GENERAIS_POSSIVEIS:
                general_escolhido = deck_generais[int(entrada)-1]
                general_escolhidos.append(general_escolhido)
                break
            elif entrada in NOMES_GENERAIS_POSSIVEIS:
                a = NOMES_GENERAIS_POSSIVEIS.index(entrada)
                b = NUMERO_GENERAIS_CORRESPODENTES[a]
                general_escolhido = deck_generais[b]
                general_escolhidos.append(general_escolhido)
            else:
                input("Véi um nome de genereal valido ou um numero de um a cinco, por favor")
                'sleep(1)'
    return general_escolhidos