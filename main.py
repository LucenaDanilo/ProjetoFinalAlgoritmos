from acoes_tabuleiro import *
from acoes_deck import *
from mensagens_usuario import *
from constantes import *

# Iniciando o Jogo
#MensagemInicial()

# Recebendo o nome dos jogadores
j1: str = 'Danilo'
j2: str = 'Andre'

#j1, j2 = ReceberNomesJogadores()
nomes_jogadores = (j1, j2)

# Dando a opção de pular o tutorial
#pular = PularTutorial()

# Passando algumas informações importantes para os jogadores
#if pular == False:
#    InstrucoesIniciais()
#    InstrucoesPreJogo()

# Iniciando a vida dos jogadores
v1, v2 = VIDA_INICIAL_JOGADORES, VIDA_INICIAL_JOGADORES

# Inicianlizando os decks dos jogadores
#if pular == True:
#    pass

# Retirando os decks do j1 e j2 a partir de um deck base
deck_jogo = deck
deck_j1 = GerarDeckJogador(deck_jogo, j1)
deck_j2 = GerarDeckJogador(deck_jogo, j2)

# Inicializando as mãos dos jogadores
MensagemMaoInicial()
mao_j1, deck_j1 = GerarMãoInicial(deck_j1, N_CARTAS_INICIAL, j1)
mao_j2, deck_j2 = GerarMãoInicial(deck_j2, N_CARTAS_INICIAL, j2)
listas_decks = [deck_j1, deck_j2]
listas_maos  = [mao_j1, mao_j2]

# Criando e exibindo o tabuleiro
tabuleiro = FazerTabuleiro()
matriz_cartas = FazerMatrizCartas()
PrintarTabuleiro(tabuleiro, j1, j2)

# Dando inicio ao jogo
jogador_turno = 1
indice_jogador_turno = 0
while True:
    # Condição que garante a alternancia entre os jogadores
    if jogador_turno > N_JOGADORES:
        jogador_turno = 1
        indice_jogador_turno = 0

    # Inicializando três variáveis para o jogador do turno
    nome_jogador = nomes_jogadores[indice_jogador_turno]
    mao_jogador = listas_maos[indice_jogador_turno]
    deck_jogador = listas_decks[indice_jogador_turno]

    # Dando início ao turno, sacando e apresentando a mão atual do jogador da vez
    MensagemTurno(indice_jogador_turno, nomes_jogadores)
    Sacar(mao_jogador, deck_jogador, nome_jogador)
    ApresentarMaoAtual(mao_jogador, nome_jogador)

    carta_escolhida = ReceberCartaEscolhida(mao_jogador, nome_jogador)
    tabuleiro = PosicionarCarta(carta_escolhida, jogador_turno, tabuleiro, nomes_jogadores, matriz_cartas)

    tabuteiro = Batalha(tabuleiro, j1, j2, jogador_turno, matriz_cartas)

    v1 -= 2
    if v1 <= 0 or v2 <= 0:
        break

    jogador_turno += 1
    indice_jogador_turno += 1