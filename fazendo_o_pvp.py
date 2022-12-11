from main_andre_lindo import *
alcance_guerreiro = 1
alcance_arqueiro = 2
alcance_catapulta = 3

def faz_turno_ataque():
    for i in range(6):
        for c in range(5):
            if i == 0 or i == 5:
                alcance = alcance_catapulta
            if i == 1 or i == 4:
                alcance = alcance_arqueiro
            if i == 3 or i == 2:
                alcance = alcance_guerreiro
            if i < 3:
                if tabuleiro[i][c] != " ":
                    for k in range(alcance):
                        posição_inimigo = k + alcance
                        if tabuleiro[posição_inimigo][c] != " ":
                            carta1_vida_inimigo = carta1_vida_inimigo - dano_atk
                            break
faz_turno_ataque()