from time import sleep
from constantes import * 
from acoes_deck import alcances
from random import randrange
from cartas import GENERAL, ARQUEIRO, GUERREIRO, CATAPULTA

# FAZ A MATRIZ DO TABULEIRO
def fazer_tabuleiro():
    matriz = []
    for i in range(NUMERO_LINHAS):
        lista = []
        for c in range(NUMERO_COLUNAS):
            lista.append(" "*7)
        matriz.append(lista)
    return matriz

def fazer_matriz_cartas():
    matriz = []
    for i in range(NUMERO_LINHAS):
        lista = []
        for c in range(NUMERO_COLUNAS):
            lista.append(0)
        matriz.append(lista)
    return matriz

# PRINTA O TABULEIRO
def printar_tabuleiro(tabuleiro, j1, j2):
    numeros_verticais = [3,2,1,1,2,3]
    indice = 0
    #sleep(2)
    for i in range(len(tabuleiro)):
        if i == 3:
            espacos = " "*43
            print("{}{}{}{}".format(cores["verde"], espacos, j1, cores["limpa"]))
            print("{}  x".format(espacos))
            print("{}{}{}{}".format(cores["azul"],espacos,j2,cores["limpa"]))
            print("――――――――――――――――――――――――"*3)
        if i == 0:
            print("     Colunas   ", end="")
            print(" "*10, end="")
            print("A         B         C         D         E")
            print("――――――――――――――――――――――――"*3)
        for c in range(5):
            if c == 0:
                if i >= 3:
                    print(f"Número da linha ({numeros_verticais[indice]}) | ", end="")
                    indice += 1
                    print("{}{}{}".format(cores["azul"], tabuleiro[i][c], cores["limpa"]), end=" | ")
                else:
                    print(f"Número da linha ({numeros_verticais[indice]}) | ", end="")
                    indice += 1
                    print("{}{}{}".format(cores["verde"], tabuleiro[i][c], cores["limpa"]), end=" | ")
            elif c<4:
                if i >= 3:
                    print("{}{}{}".format(cores["azul"], tabuleiro[i][c], cores["limpa"]), end=" | ")
                else:
                    print("{}{}{}".format(cores["verde"], tabuleiro[i][c], cores["limpa"]), end=" | ")
            else:
                if i >= 3:
                    print("{}{}{}".format(cores["azul"], tabuleiro[i][c], cores["limpa"]), end="")
                    print(" |")
                else:
                    print("{}{}{}".format(cores["verde"], tabuleiro[i][c], cores["limpa"]), end="")
                    print(" |")

        print("――――――――――――――――――――――――"*3)
        if i == 5:
            print("   Colunas     ", end="")
            print(" " * 10, end="")
            print("A         B         C         D         E")
    print()
    
def colocar_general(tabuleiro, matriz_cartas, g1, g2):
    input("No inicio de cada jogo, os generais são posicionados de maneira aleatória ")

    # Randomizando a posição dos generais
    a = randrange(3)
    b = randrange(5)
    c = randrange(3, 6)
    d = randrange(5)

    # Dando mensagem pro usuário
    input("Posicionando o general {} do jogador 1".format(g1["Nome"].capitalize())+'\n')
    sleep(1)
    input("Posicionando o general {} do jogador 2".format(g2["Nome"].capitalize())+'\n')
    sleep(1)
    
    # Inserindo o general no tabuleiro de visualização
    tabuleiro[a][b] = 'G. '+g1["Nome"][0].upper()+" "+str(g1["Vida"])
    tabuleiro[c][d] = 'G. '+g2["Nome"][0].upper()+" "+str(g2["Vida"])

    # Inserindo o general na matriz de combate
    matriz_cartas[a][b] = g1
    matriz_cartas[c][d] = g2
    return [tabuleiro, matriz_cartas, [[a,b], [c,d]]]

def posicionar_carta(carta_escolhida, jogador_turno, tabuleiro, nomes_jogadores, matriz_cartas):
    j1 = nomes_jogadores[0]
    j2 = nomes_jogadores[1]
    printar_tabuleiro(tabuleiro, j1, j2)
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
    sleep(2)
    tabuleiro[linha][colunas[col]] = carta_escolhida["Nome"][0]+" "+(" "*ajuste_espaco_branco)+str(carta_escolhida["Ataque"])+"/"+str(carta_escolhida["Vida"])
    matriz_cartas[linha][colunas[col]] = carta_escolhida
    printar_tabuleiro(tabuleiro, j1, j2)
    return [tabuleiro, matriz_cartas]

def posicionar_pos_danos(tabuleiro, matriz_cartas, linha, col, carta):
    ajuste_espaco_branco = 4 - (len(str(carta["Vida"]))+len(str(carta["Ataque"])))

    tabuleiro[linha][col] = carta["Nome"][0]+" "+(" "*ajuste_espaco_branco)+str(carta["Ataque"])+"/"+str(carta["Vida"])
    matriz_cartas[linha][col] = carta
    return [tabuleiro, matriz_cartas]

def posicionar_general_pos_danos(tabuleiro, matriz_cartas, linha, col, g):
    tabuleiro[linha][col] = 'G. '+g["Nome"][0].upper()+" "+str(g["Vida"])
    matriz_cartas[linha][col] = g
    return [tabuleiro, matriz_cartas]

def Batalha(tabuleiro, j1, j2, matriz_cartas, v1, v2):
    print()
    input("Agora iniciaremos a batalha")
    #sleep(0.3)
    print(f"Vida do jogador 1: {v1}")
    #sleep(0.3)
    print(f"Vida do jogador 2: {v2}"+"")

    cartas_mortas = []
    for row in range(len(tabuleiro)):
        for col in range(len(tabuleiro[row])):
            carta_na_posicao = matriz_cartas[row][col]

            if carta_na_posicao != 0: # Existe uma carta naquele lugar
                achou_inimigo = False
                alcance_da_carta_na_posicao = alcances[matriz_cartas[row][col]["Classe"]]
                for i in range(alcance_da_carta_na_posicao):
                    # A "linha de interesse" serve para variar entre o campo 1 e 2
                    # Para j1 -> varia entre as linhas 3, 4 e 5
                    # para j2 -> varia entre as linhas 2, 1 e 0
                    if row < 3: # A carta atacante é do j1
                        linha_interesse = 3+i
                    else:       # A carta atacante é do j2
                        linha_interesse = 2-i

                    carta_inimiga = matriz_cartas[linha_interesse][col]
                    if carta_inimiga != 0: # Tem um inimigo ali
                        achou_inimigo = True
                        # O atacante inflige dano no atacado
                        matriz_cartas[linha_interesse][col]["Vida"] -= matriz_cartas[row][col]["Ataque"] 

                        # Verificando se a carta morreu
                        if matriz_cartas[linha_interesse][col]["Vida"] > 0:
                            if matriz_cartas[linha_interesse][col]["Classe"] != GENERAL:
                                tabuleiro, matriz_cartas = posicionar_pos_danos(tabuleiro, matriz_cartas, linha_interesse, col, matriz_cartas[linha_interesse][col])
                            else:
                                tabuleiro, matriz_cartas = posicionar_general_pos_danos(tabuleiro, matriz_cartas, linha_interesse, col, matriz_cartas[linha_interesse][col])
                        else:
                            cartas_mortas.append([linha_interesse, col])
                        # O break é necessário, pois, encontrando um inimigo, a carta só ataca 1x
                        break
                if achou_inimigo == False:
                    # Se não encontrou ninguém, vai bater no inimigo
                    if row < 3: # o atacante é do j1
                        v2 -= matriz_cartas[row][col]["Ataque"] 
                        print(f'{matriz_cartas[row][col]} bateu direto na cabeça do j2, vida atual: {v2}')
                    else: # o atacante é do j2
                        v1 -= matriz_cartas[row][col]["Ataque"]
                        print(f'{matriz_cartas[row][col]} bateu firme na cabeça do j1, vida atual: {v1}')

    # Após acabar a batalha, esse laço irá retirar todas as cartas que morreram
    for carta in cartas_mortas:
        linha_int = carta[0]
        coluna_int = carta[1]
        matriz_cartas[linha_int][coluna_int] = 0
        tabuleiro[linha_int][coluna_int] = " "*7

    printar_tabuleiro(tabuleiro, j1, j2)   
    return [tabuleiro, matriz_cartas, v1, v2]

def movimenta_general(g, x_g, y_g, matriz_cartas, tabuleiro, jogador_turno, j1, j2):
    # x_g é a posição x do general em indice
    # y_g é a posição y do general em indice

    printar_tabuleiro(tabuleiro, j1, j2)

    lista_jogadores = [j1, j2]
    print("Insira a coluna e a linha, ex: A1")
    posicao = input("{}, para qual posição você deseja mover seu general?".format(lista_jogadores[jogador_turno-1])+"\n")
    while True:
        if len(posicao) != 2:
            posicao = input("Por favor, insira uma entrada de tamanho valido" +
                            '\n')
            continue
        else:
            col = posicao[0].upper()
            row = posicao[1]
        if col.upper() not in COL_VALIDA:
            posicao = input("Por favor, uma coluna valida" + '\n')
            continue
        elif row not in LINHA_VALIDA:
            posicao = input("Por favor, insira uma linha valida" + '\n')
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

        # Verificando se há uma carta na posição desejada
        colunas = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
        if (x_g == colunas[col]) and (y_g == linha):
            posicao = input("Você está inserindo sua própria posição, mas você deve se mover!"+'\n')
            continue
        elif matriz_cartas[linha][colunas[col]] != 0:
            posicao = input("Ja existe uma carta nessa posicao, por gentileza insira outra!"+'\n')
            continue
        # Verificando se a distância do passo é válida
        # O passo só pode ser de 1 de distância e não pode bater nas paredes
        if abs(x_g - colunas[col]) > 1:
            posicao = input(
                "Você está querendo dar um passo maior que a perna, insira outra posição!"
                + '\n')
            continue
        elif abs(y_g - linha) > 1:
            posicao = input(
                "Você está querendo dar um passo maior que a perna, insira outra posição!"
                + '\n')
            continue

        break

    print("Posição válida! Movimentando o seu general")
    # sleep(1)
    # Colocando o general em ambas as matrizes
    tabuleiro[linha][colunas[col]] = 'G. '+g["Nome"][0].upper()+" "+str(g["Vida"])
    matriz_cartas[linha][colunas[col]] = g

    # Retirando o general das antigas posicoes
    tabuleiro[y_g][x_g] = ' '*7
    matriz_cartas[y_g][x_g] = 0
    printar_tabuleiro(tabuleiro, j1, j2)
    return [matriz_cartas, tabuleiro, colunas[col], linha]

# Criando os feitiços
def feitico_ataque_direto(matriz_cartas, tabuleiro, jogador_turno, j1, j2):
    input("Você selecionou o feitiço: Não gostei de você")
    input("Para cada classe ele difere um dano diferente, sendo assim:"+"\n")
    print("Guerreiros: Sofrem 35 de dano")
    print("Arqueiros: Sofrem 15 de dano")
    print("Catapultas: Sofrem 16 de dano")
    print("General: Sofrem 50 de dano"+"\n")

    printar_tabuleiro(tabuleiro, j1, j2)

    print("Digite a posicao da carta, ex: A1")
    posicao = input("Selecione uma carta inimiga para sofrer um dano direto aos seus pontos de vida"+"\n")

    while True:
        # Conferindo a entrada do usuário
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
        
        # Ajustando para o j1 e j2
        if jogador_turno == 2:
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

        colunas = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
        if matriz_cartas[linha][colunas[col]] == 0:
            posicao = input(f"Não existe uma carta nessa posicao, por gentileza insira outra posição"+'\n')
            continue
        else:
            break

    # Encontrando a classe para aplicar o dano correspondente
    if matriz_cartas[linha][colunas[col]]["Classe"] == GUERREIRO:
        matriz_cartas[linha][colunas[col]]["Vida"] -= 35
    elif matriz_cartas[linha][colunas[col]]["Classe"] == ARQUEIRO:
        matriz_cartas[linha][colunas[col]]["Vida"] -= 15
    elif matriz_cartas[linha][colunas[col]]["Classe"] == CATAPULTA:
        matriz_cartas[linha][colunas[col]]["Vida"] -= 16
    else: # O inimigo é um general
        matriz_cartas[linha][colunas[col]]["Vida"] -= 50

    if matriz_cartas[linha][colunas[col]]["Classe"] != GENERAL:
        posicionar_pos_danos(tabuleiro, matriz_cartas, linha, colunas[col], matriz_cartas[linha][colunas[col]])
    else:
        posicionar_general_pos_danos(tabuleiro, matriz_cartas, linha, colunas[col], matriz_cartas[linha][colunas[col]])
    
    printar_tabuleiro(tabuleiro, j1, j2)
    return [matriz_cartas, tabuleiro]

def feitico_dia_da_reza():
    input("Nesse turno não haverá batalha!")
    return True

def feitico_atacar_duas_vezes(matriz_cartas, tabuleiro, jogador_turno, j1, j2):

    printar_tabuleiro(tabuleiro, j1, j2)
    posicao = input("Selecione a carta que você deseja que ataque duas vezes!"+"\n")

    # Verificando se a posição que o usuário informou está correta
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

        colunas = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

        if matriz_cartas[linha][colunas[col]] == 0:
            posicao = input(f"Posição inválida, não há cartas nesse local!"+'\n')
            continue
        else:
            break
    
    print("Carta selecionada, ela irá atacar o inimigo mais a frente no seu alcance!")
    
    achou_inimigo = False
    alcance_da_carta_na_posicao = alcances[matriz_cartas[linha][colunas[col]]["Classe"]]
    for i in range(alcance_da_carta_na_posicao):
        if linha < 3: # A carta atacante é do j1
            linha_interesse = 3+i
        else:       # A carta atacante é do j2
            linha_interesse = 2-i

        carta_inimiga = matriz_cartas[linha_interesse][colunas[col]]
        if carta_inimiga != 0: # Tem um inimigo ali
            achou_inimigo = True
            # O atacante inflige dano no atacado
            matriz_cartas[linha_interesse][colunas[col]]["Vida"] -= matriz_cartas[linha][colunas[col]]["Ataque"]

    if achou_inimigo == False:
        print('Infelizmente, não havia ninguém no alcance, sua carta não atacou ninguém')

    return [matriz_cartas, tabuleiro]