from time import sleep
from constantes import * 
from acoes_deck import alcances

# FAZ A MATRIZ DO TABULEIRO
def FazerTabuleiro():
    matriz = []
    for i in range(NUMERO_LINHAS):
        lista = []
        for c in range(NUMERO_COLUNAS):
            lista.append(" "*7)
        matriz.append(lista)
    return matriz

def FazerMatrizCartas():
    matriz = []
    for i in range(NUMERO_LINHAS):
        lista = []
        for c in range(NUMERO_COLUNAS):
            lista.append(0)
        matriz.append(lista)
    return matriz

# PRINTA O TABULEIRO
def PrintarTabuleiro(tabuleiro, j1, j2):
    numeros_verticais = [3,2,1,1,2,3]
    indice = 0
    #sleep(2)
    for i in range(len(tabuleiro)):
        if i == 3:
            espacos = " "*43
            print(f"{espacos}{j1} \n{espacos}  x\n{espacos}{j2}")
            print("――――――――――――――――――――――――"*3)
        if i == 0:
            print("     Colunas   ", end="")
            print(" "*10, end="")
            print("A         B         C         D         E")
            print("――――――――――――――――――――――――"*3)
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

        # print("")
        print("――――――――――――――――――――――――"*3)
        if i == 5:
            print("   Colunas     ", end="")
            print(" " * 10, end="")
            print("A         B         C         D         E")
    print()
    
#tabuleiro = faz_tabuleiro()
#printar_tabuleiro(tabuleiro)

def PosicionarCarta(carta_escolhida, jogador_turno, tabuleiro, nomes_jogadores, matriz_cartas):
    j1 = nomes_jogadores[0]
    j2 = nomes_jogadores[1]
    PrintarTabuleiro(tabuleiro, j1, j2)
    print("Ex: Para posicionar uma carta na coluna A e linha 1 digite: 'A1'")
    posicao = input("Qual a posicao que voce gostaria de inserir sua carta? Coluna/linha"+'\n')
        
    # Verificando se a entrada foi uma jogada válida
    while True:
        if len(posicao) != 2:
            posicao = input("Por favor, insira uma entrada de tamanho valido"+'\n')
            continue
        else:
            col = posicao[0].upper()
            row = posicao[1]
        if col.upper() not in COL_VALIDA:
            posicao = input("Por favor, uma coluna valida"+'\n')
            continue
        elif row not in LINHA_VALIDA:
            posicao = input("Por favor, insira uma linha valida"+'\n')
            continue

        alcance_padrao_classe = alcances[carta_escolhida["Classe"].capitalize()]
        if alcance_padrao_classe != int(row):
            posicao = input(f"Sua carta nao pode ser colocada nessa linha! Ela nao tem esse alcance, o alcance da carta é {alcance_padrao_classe}"+'\n')
            continue
        
        # Ajustando para o j1 e j2
        if jogador_turno == 1:
            if int(row) == 1:
                linha = 2
            elif int(row) == 2:
                linha = 1
            else:
                linha = 0
        else:
            if int(row) == 1:
                linha = 3
            elif int(row) == 2:
                linha = 4
            else:
                linha = 5

        ajuste_espaco_branco = 4 - (len(str(carta_escolhida["Vida"]))+len(str(carta_escolhida["Ataque"])))
        colunas = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

        if matriz_cartas[linha][colunas[col]] != 0:
            posicao = input(f"Ja existe uma carta nessa posicao, por gentileza insira outra!"+'\n')
            continue
        else:
            break


    print("Posição Válida! Posicionando sua carta..."+"\n")
    #sleep(2)
    tabuleiro[linha][colunas[col]] = carta_escolhida["Nome"][0]+" "+(" "*ajuste_espaco_branco)+str(carta_escolhida["Ataque"])+"/"+str(carta_escolhida["Vida"])
    matriz_cartas[linha][colunas[col]] = carta_escolhida
    PrintarTabuleiro(tabuleiro, j1, j2)
    return [tabuleiro, matriz_cartas]


def PosicionarPosDanos(tabuleiro, matriz_cartas, linha, col, carta):

    ajuste_espaco_branco = 4 - (len(str(carta["Vida"]))+len(str(carta["Ataque"])))

    tabuleiro[linha][col] = carta["Nome"][0]+" "+(" "*ajuste_espaco_branco)+str(carta["Ataque"])+"/"+str(carta["Vida"])
    matriz_cartas[linha][col] = carta
    return [tabuleiro, matriz_cartas]

def Batalha(tabuleiro, j1, j2, matriz_cartas, v1, v2):
    input("Agora iniciaremos a batalha")

    for row in range(len(tabuleiro)):
        for col in range(len(tabuleiro[row])):
            carta_na_posicao = matriz_cartas[row][col]
            if carta_na_posicao != 0: # Existe uma carta naquele lugar
                achou_inimigo = False
                alcance_da_carta_na_posicao = alcances[matriz_cartas[row][col]["Classe"]]
                for i in range(alcance_da_carta_na_posicao):        
                    if row < 3: # A carta atacante é do j1
                        carta_inimiga = matriz_cartas[3+i][col]
                        if carta_inimiga != 0: # Tem um inimigo ali
                            achou_inimigo = True
                            # O atacante inflige dano no atacado
                            matriz_cartas[3+i][col]["Vida"] -= matriz_cartas[row][col]["Ataque"] 

                            # Verificando se a carta morreu
                            if matriz_cartas[3+i][col]["Vida"] > 0:
                                tabuleiro, matriz_cartas = PosicionarPosDanos(tabuleiro, matriz_cartas, 3+i, col, matriz_cartas[3+i][col])
                            else:  
                                matriz_cartas[3+i][col] = 0
                                tabuleiro[3+i][col] = " "*7
                            break
                    elif row >= 3: # A carta atacante é do j2
                        pass
                if not achou_inimigo:
                    # Se não encontrou ninguém, vai bater no inimigo
                    v2 -= matriz_cartas[row][col]["Ataque"] 
                    print(f'batando na cabeça do j2, vida atual: {v2}')
    
    PrintarTabuleiro(tabuleiro, j1, j2)   
    return [tabuleiro, matriz_cartas]
