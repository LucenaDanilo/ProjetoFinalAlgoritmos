# Projeto Algoritmos

Duel Card Game - Criação própria



# Caracerísticas Gerais


Tabuleiro de 6x4
Sendo metade para um jogador e metade para o outro. (3 linhas para cada)

-	Linha 1: Cartas do classe Corpo-a-Corpo (Menor Dano / Maior Vida) 
-	Linha 2: Cartas do classe Ataque-a-Distância (Maior dano / Menor Vida)
-	Linha 3: Cartas de longa distância && Cartas especiais (buff/debuff)

Os cards padrão, com exceção do General, não se movem.

Todas as tropas atigem a primeira tropa do outro lado (ataque por coluna)

Quando tropas do mesmo tipo se atigem, ambas levam dano

Quando uma tropa de maior range ataca uma menor, ela não toma dano.

Caso não haja uma tropa do mesmo tipo da atacante, o dano será direto no jogador.


# Settings do General


Todo jogador tem um General.
- Todo General tem algum tipo de buff sobre o tabuleiro
	- Buff na própria casa (alto buff)
	- Buff na coluna (Médio-baixo buff)
	- Buff na linha (Médio-baixo buff)

-	Movimentação:
	-	Apenas um quadrado por turno, qualquer direção.
	-	O lider apenas se move no seu campo.
	-	Obs: Movimentação obrigatória ou não.
-	O lider exerce um determinado buff
-	O lider não ataca, apenas absorve dano.
-	O lider não pode morrer, ele apenas é atordoado por x turnos.
-	Caso lider esteja numa casa com uma tropa, ambos dividem o dano.
-	Caso lider esteja numa casa com uma tropa e a tropa morrer, lider atordoado 1 round
-	Quando o lider for abatido, o oponente ganhará um buff (DECIDIR AINDA)


# Tipos de carta


-	Existirão 4 classes de cartas:
	- Corpo-a-corpo (Linha 1)
	- Médio alcance (Linha 2)
	- Longo alcance (Linha 3)
	- Especiais

Cada carta terá os seguintes atributos:
	- Nome
	- Pontos de Ataque
	- Pontos de Vida

Cada carta também poderá ter um efeito especial, podendo ser ativado por algum
pré-requisito de ativação.


# Fim de Jogo


Cada jogador tem uma quantidade de pontos de vida
Os pontos de vida podem ser alterados durante o jogo
Um jogador perde vida quando uma tropa inimiga o ataca diretamente
