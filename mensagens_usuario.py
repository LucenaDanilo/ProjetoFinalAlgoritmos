from time import sleep

def MensagemInicial():
    print("Iniciando o Jogo"+"\n")
    input("Envie qualquer coisa para iniciar! :D"+'\n')

def ReceberNomesJogadores():
    print("Usuário 1, digite seu nome abaixo"+"\n")
    while True:
        j1 = input().capitalize()
        if len(j1) > 20:
            print("Nome muito grande, repita por favor!"+"\n")
        elif len(j1) == 0:
            print("Por favor, insira algum nome"+"\n")
        elif j1.isnumeric() == True:
            print("Por favor, insira um nome com alguma letra!"+"\n")
        else:
            break
    print("Usuário 2, digite seu nome abaixo"+"\n")
    while True:
        j2 = input().capitalize()
        if len(j2) > 20:
            print("Nome muito grande, repita por favor!"+"\n")
        elif len(j2) == 0:
            print("Por favor, insira algum nome"+"\n")
        elif j2.isnumeric() == True:
            print("Por favor, insira um nome com alguma letra!"+"\n")
        else:
            break
    print("")
    print("Nomes recebidos com sucesso!")
    print("Bem vindos, "+j1+' e '+j2+'\n')
    return [j1, j2]

def PularTutorial():
    resposta = input("Voce deseja pular o nosso tutorial? (S/N)"+'\n')
    while True:
        if resposta.upper() == 'S':
            print("")
            return True
        elif resposta.upper() == 'N':
            print("")
            return False
        else:
            resposta = input("Por gentileza, envie 'S' para sim ou 'N' para nao")

def InstrucoesIniciais():
    input("O nosso jogo eh um jogo de cartas com interações/batalhas dentro de um tabuleiro 5x6")
    input("Sendo assim, cada jogador terá seu deck de cartas e a cada turno...")
    input("Cada jogador poderá posicionar suas cartas em campo para duelar com o adversário")

    print("As unidades, apos posicionadas, atacarao automaticamente ao fim do turno")
    input("Sendo benefico pra voce ou não! Fique ligado nisso")
    input("Mais instruções serão dadas a seguir! Não se preocupe!"+"\n")

def InstrucoesPreJogo():
    input("O jogo tem tres classes principais de unidades")
    input("As unidades de ataque corpo a corpo: Lutadores")
    input("As unidades de ataque a media distancia: Atiradores")
    input("As unidades de ataque a longa distancia: Armamento Pesado")
    print("")

    input("Por agora, voce apenas precisa saber que cada classe será representada de maneira especifica")
    input("E que cada classe eh posicionada em um linha especifica do tabuleiro")
    input("A representacao das classes sera seguinte forma:"+'\n')
    print("Unidades Lutadores: L")
    print("Unidades Atiradores: A")
    input("Unidades Armamento Pesado: P")

def MensagensIniciaisJogo(pulou):
    if pulou:
        input("Voce nao precisou ler as intrucoes e ja quer iniciar o jogo, vamos iniciar")
    else:
        input("Agora que voce ja leu as instrucoes iniciais, vamos iniciar")
    print("Nesse momento, ambos os decks serao embaralhados")
    print("e as maos serão servidas aos jogadores"+'\n')
    input()

def MensagemMaoInicial():
    print("Os decks de ambos os jogadores ja foram embaralhados!")
    sleep(1)
    input("Envie qualquer mensagem para dar inicio as distribuicoes das cartas iniciais dos jogadores"+'\n')

def MensagemTurno(jogador_turno, lista_nome_jogadores):
    input(f"Agora é o turno do jogador {jogador_turno+1}: {lista_nome_jogadores[jogador_turno]}"+'\n')

