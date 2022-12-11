"""3 por 4 """
numero_colunas = 5
numero_linhas = 6


# FAZ A MATRIZ DO TABULEIRO
def faz_tabuleiro():
    matriz = []
    for i in range(numero_linhas):
        lista = []
        for c in range(numero_colunas):
            lista.append(" ")
        matriz.append(lista)
    return matriz
# PRINTA O TABULEIRO
def printar_tabuleiro(tabuleiro):
    numeros_verticais = [1,2,3,3,2,1]
    indice = 0
    for i in range(len(tabuleiro)):
        if i == 3:
            print(f"{jogador_1} \n  x\n{jogador_2}")
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
jogador_1 = 'andre'
jogador_2 = 'danilo'
#tabuleiro = faz_tabuleiro()
#printar_tabuleiro(tabuleiro)