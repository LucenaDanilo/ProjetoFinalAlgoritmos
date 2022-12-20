from random import randrange
from copy import deepcopy
from constantes import *
from time import sleep

# Iniciando os Jogadores
j1 = 'Danilo'
j2 = 'André'

# Iniciando as constantes
GUERREIRO = 'Guerreiro'
ARQUEIRO = 'Arqueiro'
CATAPULTA = 'Catapulta'

# As cartas só poderão ter esses valores de ataque ou vida
PONTOS_DE_ATAQUE = [1, 2, 3, 5, 8]    # Possíveis pontos de ATAQUE para as cartas
PONTOS_DE_VIDA   = [20, 8, 12, 16, 18] # Possíveis pontos de VIDA para as cartas

# Atribuindo os valores de ataques das cartas existentes
ATAQUE_CARTA_DANILO = PONTOS_DE_ATAQUE[0]
ATAQUE_CARTA_BRUNA = PONTOS_DE_ATAQUE[0]
ATAQUE_CARTA_LUIZA = PONTOS_DE_ATAQUE[0]
ATAQUE_CARTA_ANDRE = PONTOS_DE_ATAQUE[4]
ATAQUE_CARTA_JESSICA = PONTOS_DE_ATAQUE[4]
ATAQUE_CARTA_GUSTAVO = PONTOS_DE_ATAQUE[4]
ATAQUE_CARTA_ZE = PONTOS_DE_ATAQUE[3]
ATAQUE_CARTA_IAGO = PONTOS_DE_ATAQUE[3]
ATAQUE_CARTA_AELOA = PONTOS_DE_ATAQUE[3]

# Atribuindo os valores de vidas das cartas existentes
VIDA_CARTA_DANILO = PONTOS_DE_VIDA[0]
VIDA_CARTA_BRUNA = PONTOS_DE_VIDA[0]
VIDA_CARTA_LUIZA = PONTOS_DE_VIDA[0]
VIDA_CARTA_ANDRE = PONTOS_DE_VIDA[4]
VIDA_CARTA_JESSICA = PONTOS_DE_VIDA[4]
VIDA_CARTA_GUSTAVO = PONTOS_DE_VIDA[4]
VIDA_CARTA_ZE = PONTOS_DE_VIDA[3]
VIDA_CARTA_IAGO = PONTOS_DE_VIDA[3]
VIDA_CARTA_AELOA = PONTOS_DE_VIDA[3]

# Criando as cartas
carta_danilo  = {'Classe': GUERREIRO, 'Nome': 'Danilo',  'Ataque': ATAQUE_CARTA_DANILO,  'Vida': VIDA_CARTA_DANILO, 'Turma': 'Henrique'}
carta_bruna   = {'Classe': GUERREIRO, 'Nome': 'Bruna',   'Ataque': ATAQUE_CARTA_BRUNA,   'Vida': VIDA_CARTA_BRUNA}
carta_luiza   = {'Classe': GUERREIRO, 'Nome': 'Luiza',   'Ataque': ATAQUE_CARTA_LUIZA,   'Vida': VIDA_CARTA_LUIZA}
carta_andre   = {'Classe': ARQUEIRO,  'Nome': 'Andre',   'Ataque': ATAQUE_CARTA_ANDRE,   'Vida': VIDA_CARTA_ANDRE}
carta_jessica = {'Classe': ARQUEIRO,  'Nome': 'Jessica', 'Ataque': ATAQUE_CARTA_JESSICA, 'Vida': VIDA_CARTA_JESSICA}
carta_gustavo = {'Classe': ARQUEIRO,  'Nome': 'Gustavo', 'Ataque': ATAQUE_CARTA_GUSTAVO, 'Vida': VIDA_CARTA_GUSTAVO}
carta_ze      = {'Classe': CATAPULTA, 'Nome': 'Ze',      'Ataque': ATAQUE_CARTA_ZE,      'Vida': VIDA_CARTA_ZE}
carta_iago    = {'Classe': CATAPULTA, 'Nome': 'Iago',    'Ataque': ATAQUE_CARTA_IAGO,    'Vida': VIDA_CARTA_IAGO}
carta_aeloa   = {'Classe': CATAPULTA, 'Nome': 'Aeloa',   'Ataque': ATAQUE_CARTA_AELOA,   'Vida': VIDA_CARTA_AELOA}

# Setando os alcances
alcances = {GUERREIRO: 1, ARQUEIRO: 2, CATAPULTA: 3}

# Inicializando o deck
deck = [carta_danilo, carta_bruna, carta_luiza, carta_andre , carta_jessica, carta_gustavo, carta_ze, carta_iago, carta_aeloa]

# A função abaixo é responsável por embaralhar as cartas para um jogador receber seu deck de cartas
def GerarDeckJogador(deck, nome_jogador):
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
def GerarMãoInicial(deck_jogador, n_cartas, nome_jogador):
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
def ApresentarMaoAtual(mao_atual, nome_jogador):
    print(nome_jogador+', sua mao atual eh a seguinte:')
    print('')

    cont = 1
    for carta in mao_atual:
        print(str(cont)+'. '+carta['Nome']+': Classe: '+carta['Classe']+' | ATK: '+str(carta['Ataque'])+' | VIDA: '+str(carta['Vida']))
        #sleep(0.8)
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
    #sleep(1)

    while True:
        if indice_carta not in INDICE_CARTA_POSSIVEL:
            indice_carta = input("Por gentileza, insira um numero valido"+"\n").strip()
        else:
            indice_carta = int(indice_carta)
            break
        
    carta_jogada = mao_atual.pop(indice_carta-1)
    print("Voce escolheu a carta: "+carta_jogada["Nome"])
    return carta_jogada
