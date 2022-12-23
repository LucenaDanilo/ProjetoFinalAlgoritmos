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

# Apresentando a opção de conhecer os generais
#sleep(1)
#conhecer_generais = mensagem_general1()

# Passando informações sobre os generais se solicitado
#if conhecer_generais:
#    explicando_generais()

# Retirando os decks do j1 e j2 a partir de um deck base
deck_jogo = deck
deck_j1 = gerar_deck_jogador(deck_jogo, j1)
deck_j2 = gerar_deck_jogador(deck_jogo, j2)

# Inicializando as mãos dos jogadores
MensagemMaoInicial()
mao_j1, deck_j1 = gerar_mao_inicial(deck_j1, N_CARTAS_INICIAL, j1)
mao_j2, deck_j2 = gerar_mao_inicial(deck_j2, N_CARTAS_INICIAL, j2)
listas_decks = [deck_j1, deck_j2]
listas_maos  = [mao_j1, mao_j2]

# Criando e exibindo o tabuleiro
tabuleiro = fazer_tabuleiro()
matriz_cartas = fazer_matriz_cartas()

# Selecionando e inserindo os generais no jogo
g1 = general_henrique
g2 = general_iana
tabuleiro, matriz_cartas, posicoes_generais = colocar_general(tabuleiro, matriz_cartas, g1, g2)
x_g1, y_g1 = posicoes_generais[0][1], posicoes_generais[0][0]
x_g2, y_g2 = posicoes_generais[1][1], posicoes_generais[1][0]
lista_generais = [g1, g2]
printar_tabuleiro(tabuleiro, j1, j2)

# Dando inicio ao jogo
jogador_turno = 1
indice_jogador_turno = 0
while True:
    # Condição que garante a alternancia entre os jogadores
    if jogador_turno > N_JOGADORES:
        jogador_turno = 1
        indice_jogador_turno = 0

    # Inicializando algumas variáveis para o jogador do turno
    nome_jogador = nomes_jogadores[indice_jogador_turno]
    general_turno = lista_generais[indice_jogador_turno]
    # mao_jogador = listas_maos[indice_jogador_turno]
    # deck_jogador = listas_decks[indice_jogador_turno]

    # Dando início ao turno, sacando e apresentando a mão atual do jogador da vez
    MensagemTurno(indice_jogador_turno, nomes_jogadores)


    listas_maos[indice_jogador_turno], listas_decks[indice_jogador_turno] = Sacar(listas_maos[indice_jogador_turno], listas_decks[indice_jogador_turno], nome_jogador)
    apresentar_mao_atual(listas_maos[indice_jogador_turno], nome_jogador)

    # Recebendo a carta e posicionando ela no tabuleiro
    carta_escolhida = ReceberCartaEscolhida(listas_maos[indice_jogador_turno], nome_jogador)
    tabuleiro, matriz_cartas = posicionar_carta(carta_escolhida, jogador_turno, tabuleiro, nomes_jogadores, matriz_cartas)

   
    # Garantindo que a batalha só acontece após os dois jogadores jogarem
    if jogador_turno == 2:
        # Trabalhando com a posição dos generais pré batalha
        matriz_cartas, tabuleiro, x_g1, y_g1 = movimenta_general(g1, x_g1, y_g1, matriz_cartas, tabuleiro, 1, j1, j2)
        matriz_cartas, tabuleiro, x_g2, y_g2 = movimenta_general(g2, x_g2, y_g2, matriz_cartas, tabuleiro, 2, j1, j2)

        tabuteiro, matriz_cartas, v1, v2 = Batalha(tabuleiro, j1, j2, matriz_cartas, v1, v2)

    # A única condição do jogo acabar é caso um dos jogadores morra
    if v1 <= 0 or v2 <= 0:
        break

    jogador_turno += 1
    indice_jogador_turno += 1

mensagem_fim_de_jogo(v1, v2)
