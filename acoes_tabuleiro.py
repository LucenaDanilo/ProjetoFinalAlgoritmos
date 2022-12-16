from time import sleep
from constantes import * 

# FAZ A MATRIZ DO TABULEIRO
def FazerTabuleiro():
    matriz = []
    for i in range(NUMERO_LINHAS):
        lista = []
        for c in range(NUMERO_COLUNAS):
            lista.append(" ")
        matriz.append(lista)
    return matriz
# PRINTA O TABULEIRO
def PrintarTabuleiro(tabuleiro, j1, j2):
    numeros_verticais = [1,2,3,3,2,1]
    indice = 0
    sleep(2)
    for i in range(len(tabuleiro)):
        if i == 3:
            espacos = " "*28
            print(f"{espacos}{j1} \n{espacos}  x\n{espacos}{j2}")
            #print("―――――――――――――――――――――――――――")
        if i == 0:
            print("     Colunas", end="")
            print(" "*10, end="")
            print("A   B   C   D   E")
            #print("―――――――――――――――――――――――――――")
        for c in range(5):
            if c == 0:
                print(f"Número da linha ({numeros_verticais[indice]}) | ", end="")
                indice += 1
                print(tabuleiro[i][c], end=" | ")
            elif c<4:
                print(tabuleiro[i][c], end=" | ")
            else:

                print(tabuleiro[i][c], end="")
                print(" |")

        #print("―――――――――――――――――――――――――――")
        if i == 5:
            print("     Colunas", end="")
            print(" " * 10, end="")
            print("A   B   C   D   E")
    print()
    
#tabuleiro = faz_tabuleiro()
#printar_tabuleiro(tabuleiro)

def PosicionarCarta(carta_escolhida, jogador_turno, tabuleiro, nomes_jogadores):
    j1 = nomes_jogadores[0]
    j2 = nomes_jogadores[1]
    PrintarTabuleiro(tabuleiro, j1, j2)
    print("Ex: Para posicionar uma carta na coluna A e linha 1 digite: 'A1'")
    posicao = input("Qual a posicao que voce gostaria de inserir sua carta? Coluna/linha"+'\n')
    
    # Verificando se a entrada foi uma jogada válida
    while True:
        if len(posicao) != 2:
            posicao = input("Por favor, insira uma entrada de tamanho valido"+'\n')
        elif posicao[0].upper() not in COL_VALIDA:
            posicao = input("Por favor, uma coluna valida"+'\n')
        elif posicao[1] not in LINHA_VALIDA:
            posicao = input("Por favor, insira uma linha valida"+'\n')
        else:
            break
    