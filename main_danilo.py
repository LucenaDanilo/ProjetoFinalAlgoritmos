from random import randrange
from copy import deepcopy

# Iniciando as constantes
GUERREIRO = 'guerreiro'
ARQUEIRO = 'arqueiro'
CATAPULTA = 'catapulta'

PONTOS_DE_ATAQUE = [10, 20, 30, 40, 50]    # Possíveis pontos de ATAQUE para as cartas
PONTOS_DE_VIDA   = [40, 80, 120, 160, 180] # Possíveis pontos de VIDA para as cartas
    
# Atribuindo os ataques das cartas existentes
ATAQUE_CARTA_DANILO = PONTOS_DE_ATAQUE[0]
ATAQUE_CARTA_ANDRE = PONTOS_DE_ATAQUE[4]
ATAQUE_CARTA_ZE = PONTOS_DE_ATAQUE[3]

# Atribuindo as vidas das cartas existentes
VIDA_CARTA_DANILO = PONTOS_DE_VIDA[0]
VIDA_CARTA_ANDRE = PONTOS_DE_VIDA[4]
VIDA_CARTA_ZE = PONTOS_DE_VIDA[3]

# Criando as cartas

carta_danilo = {'Classe': GUERREIRO, 'Nome': 'Danilo', 'Ataque': ATAQUE_CARTA_DANILO, 'Vida': VIDA_CARTA_DANILO}
carta_andre = {'Classe': ARQUEIRO, 'Nome': 'Andre', 'Ataque': ATAQUE_CARTA_ANDRE, 'Vida': VIDA_CARTA_ANDRE}
carta_ze = {'Classe': CATAPULTA, 'Nome': 'Ze', 'Ataque': ATAQUE_CARTA_ZE, 'Vida': VIDA_CARTA_ZE}

# Inicializando o deck

deck = [carta_danilo, carta_andre, carta_ze]

def GerarCartasInicial(nome_jogador):
    mao_jogador = []
    while True:
        passo = randrange(-50,50)
        if passo != 0:
            break

    for i in range(0, len(deck), passo):
        posicao = randrange(len(deck))
        mao_jogador.insert(posicao,deck[i])
    return mao_jogador

mao_jogador1 = GerarCartasInicial('Danilo')
print(mao_jogador1)