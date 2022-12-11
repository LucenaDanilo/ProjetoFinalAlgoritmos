from main_andre_lindo import faz_tabuleiro, printar_tabuleiro
from main_danilo import deck, GerarDeckJogador
from mensagens_usuario import *

# Iniciando o Jogo
MensagemInicial()

# Recebendo o nome dos jogadores
j1: str = ''
j2: str = ''

j1, j2 = ReceberNomesJogadores()

# Dando a opção de pular o tutorial
pular = PularTutorial()

# Passando algumas informações importantes para os jogadores
if pular == False:
    InstrucoesIniciais()
    InstrucoesPreJogo()