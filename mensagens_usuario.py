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
            resposta = input("Por gentileza, envie 'S' para sim ou 'N' para nao"+'\n')

def InstrucoesIniciais():
    input("O nosso jogo eh um jogo de cartas com interações/batalhas dentro de um tabuleiro 5x6")
    input("Sendo assim, cada jogador terá seu deck de cartas...")
    input("Cada jogador poderá posicionar suas cartas em campo para duelar com o adversário")

    print("As unidades, apos posicionadas, atacarao automaticamente ao fim do turno")
    input("Sendo benefico pra voce ou não! Fique ligado nisso")
    input("Mais instruções serão dadas a seguir! Não se preocupe!"+"\n")

def InstrucoesPreJogo():
    input("O jogo tem tres classes principais de unidades")
    input("As unidades de ataque corpo a corpo: Guerreiros")
    input("As unidades de ataque a media distancia: Arqueiros")
    input("As unidades de ataque a longa distancia: Catapultas")
    print("")

    input("Por agora, voce apenas precisa saber que cada classe será representada de maneira especifica")
    input("E que cada classe eh posicionada em um linha especifica do tabuleiro")
    input("A representacao das classes sera seguinte forma:"+'\n')
    print("Unidades Guerreiros: G")
    print("Unidades Arqueiro: A")
    input("Unidades Catapulta: C")

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

def mensagem_general1():
        sleep(1)
        input("Atualmente estamos com 5 generais no jogo, cada qual com sua particularidade")
        sleep(1)
        resposta = input("Deseja conhecer um pouco sobre suas funcionalidades? (S/N)""\n")
        while True:
            if resposta.upper() == 'S':
                print("")
                return True
            elif resposta.upper() == 'N':
                print("")
                return False
            else:
                resposta = input("Por gentileza, envie 'S' para sim ou 'N' para nao")

def explicando_generais():
    sleep(1)
    input("Decidimos que os generais seriam as únicas peças moveis desse card game.""\n"
          "Eles servirão como tanks do game (70 de vida), e serão úteis em diferentes contextos"
          " e de diferententes formas.")
    input("Atualmente temos 5 generais, sendo 3 deles personagens históricos e"
          " dois deles professores.")
    input("Os 3 generais históricos possuem certos 'buffs' e 'debuffs' diferentes entre si""\n"
          "Já os outros dois possuem características compartilhadas.")

    input("São eles:")
    input("Alexandre,O Grande e seu poder de ressureição.""\n"
          "Se sua vida chegar a 0 um dano é infligido diretamente na vida do jogador.")
    print()
    sleep(1)
    input("Rei Lêonidas.""\n""Dá coragem a um guerreiro aumentando seu alcance e seu dano em batalha.""\n"
          "Se sua vida chegar a zero a coragem dos guerreiros se esvai perdendo vida.")
    print()
    sleep(1)
    input("Gengis Khan.""\n""Devido a suas invenções, sua presença em campo de batalha dá a chance de um duplo ataque"
          " dos arqueiros.""\n""Sua morte causa um alto dano à vida do jogador.")
    print()
    sleep(1)
    input("Henrique e Iana.""\n""Colocamos os professores de programação como dois dos generais.""\n"
          "Como as cartas são seus alunos, o buff é aplicado nos alunos que pertecerem a turma "
          "do professor.""\n""Se a vida chegar a zero o buff é substituido por um debuff de mesmo valor.")
    print()

def MensagemTurno(jogador_turno, lista_nome_jogadores):
    input(f"Agora é o turno do jogador {jogador_turno+1}: {lista_nome_jogadores[jogador_turno]}"+'\n')

def mensagem_fim_de_jogo(v1, v2):
    print('Fim de Jogo!')