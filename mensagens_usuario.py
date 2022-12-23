from constantes import CORES
from time import sleep

def mensagem_inicial():
    print('''
████████████████████████████████████████████████████████████████████████████████████████████
█▄─▄─▀█▄─▄▄─█▄─▀█▀─▄███▄─█─▄█▄─▄█▄─▀█▄─▄█▄─▄▄▀█─▄▄─████▀▄─██─▄▄─███▄─▄▄▀█▄─██─▄█▄─▄▄─█▄─▄███
██─▄─▀██─▄█▀██─█▄█─█████▄▀▄███─███─█▄▀─███─██─█─██─████─▀─██─██─████─██─██─██─███─▄█▀██─██▀█
▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▀▀▀▄▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▀▀▀▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀
███████████████████████████████▀███████████████████████
█─▄▄▄─██▀▄─██▄─▄▄▀█▄─▄▄▀███─▄▄▄▄██▀▄─██▄─▀█▀─▄█▄─▄▄─█░█
█─███▀██─▀─███─▄─▄██─██─███─██▄─██─▀─███─█▄█─███─▄█▀█▄█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▀
    ''')
    print()
    print("******************************************")
    print("{}Iniciando o Jogo{}".format(CORES["vermelho"], CORES["limpa"]))
    print("{}Envie qualquer coisa para iniciar! :D{}".format(CORES["vermelho"], CORES["limpa"]))
    input("****************************************** ")

def ReceberNomesJogadores():
    print("{}Usuário 1, digite seu nome abaixo{}".format(CORES["cinza"], CORES["limpa"])+"\n")
    while True:
        j1 = input().capitalize()
        if len(j1) > 20:
            print("{}Nome muito grande, repita por favor!{}".format(CORES["vermelho"], CORES["limpa"])+"\n")
        elif len(j1) == 0:
            print("{}Por favor, insira algum nome{}".format(CORES["vermelho"], CORES["limpa"])+"\n")
        elif j1.isnumeric() == True:
            print("{}Por favor, insira um nome com alguma letra!{}".format(CORES["vermelho"], CORES["limpa"])+"\n")
        else:
            break
    print("{}Usuário 2, digite seu nome abaixo{}".format(CORES["cinza"], CORES["limpa"])+"\n")
    while True:
        j2 = input().capitalize()
        if len(j2) > 20:
            print("{}Nome muito grande, repita por favor!{}".format(CORES["vermelho"], CORES["limpa"])+"\n")
        elif len(j2) == 0:
            print("{}Por favor, insira algum nome{}".format(CORES["vermelho"], CORES["limpa"])+"\n")
        elif j2.isnumeric() == True:
            print("{}Por favor, insira um nome com alguma letra!{}".format(CORES["vermelho"], CORES["limpa"])+"\n")
        else:
            break
    print("")
    print("{}Nomes recebidos com sucesso!{}".format(CORES["cinza"], CORES["limpa"]))
    print("{}Bem vindos, {}".format(CORES["cinza"], CORES["limpa"])+j1+' e '+j2+'\n')
    return [j1, j2]

def PularTutorial():
    resposta = input("{}Voce deseja pular o nosso tutorial? (S/N){}".format(CORES["cinza"], CORES["limpa"])+'\n')
    while True:
        if resposta.upper() == 'S':
            print("")
            return True
        elif resposta.upper() == 'N':
            print("")
            return False
        else:
            resposta = input("{}Por gentileza, envie 'S' para sim ou 'N' para nao{}".format(CORES["vermelho"], CORES["limpa"])+'\n')

def InstrucoesIniciais():
    input("{}O nosso jogo eh um jogo de cartas com interações/batalhas dentro de um tabuleiro 5x6{}".format(CORES["cinza"], CORES["limpa"]))
    input("{}Sendo assim, cada jogador terá seu deck de cartas...{}".format(CORES["cinza"], CORES["limpa"]))
    input("{}Cada jogador poderá posicionar suas cartas em campo para duelar com o adversário{}".format(CORES["cinza"], CORES["limpa"]))

    print("{}As unidades, apos posicionadas, atacarao automaticamente ao fim do turno{}".format(CORES["cinza"], CORES["limpa"]))
    input("{}Sendo benefico pra voce ou não! Fique ligado nisso{}".format(CORES["cinza"], CORES["limpa"]))
    input("{}Mais instruções serão dadas a seguir! Não se preocupe!{}".format(CORES["cinza"], CORES["limpa"])+"\n")

def InstrucoesPreJogo():
    input("{}O jogo tem tres classes principais de unidades{}".format(CORES["cinza"], CORES["limpa"]))
    input("{}As unidades de ataque corpo a corpo: Guerreiros{}".format(CORES["cinza"], CORES["limpa"]))
    input("{}As unidades de ataque a media distancia: Arqueiros{}".format(CORES["cinza"], CORES["limpa"]))
    input("{}As unidades de ataque a longa distancia: Catapultas{}".format(CORES["cinza"], CORES["limpa"]))
    print("")

    input("{}Por agora, voce apenas precisa saber que cada classe será representada de maneira especifica{}".format(CORES["cinza"], CORES["limpa"]))
    input("{}E que cada classe eh posicionada em um linha especifica do tabuleiro{}".format(CORES["cinza"], CORES["limpa"]))
    input("{}A representacao sera seguinte forma:{}".format(CORES["cinza"], CORES["limpa"])+'\n')
    print("{}Caso a carta no tabuleiro seja: André | Ataque: 10 | Vida: 50{}".format(CORES["cinza"], CORES["limpa"]))
    input("{}Sua representação será: A 10/50 {}".format(CORES["cinza"], CORES["limpa"]))

def MensagensIniciaisJogo(pulou):
    if pulou:
        input("Voce nao precisou ler as intrucoes e ja quer iniciar o jogo, vamos iniciar")
    else:
        input("Agora que voce ja leu as instrucoes iniciais, vamos iniciar")
    print("Nesse momento, ambos os decks serao embaralhados")
    print("e as maos serão servidas aos jogadores"+'\n')
    input()

def MensagemMaoInicial():
    print("{}Os decks de ambos os jogadores ja foram embaralhados!{}".format(CORES["amarelo"], CORES["limpa"]))
    sleep(1)
    input("{}Envie qualquer mensagem para dar inicio as distribuicoes das cartas iniciais dos jogadores{}".format(CORES["amarelo"], CORES["limpa"])+'\n')

def mensagem_general1():
        sleep(1)
        input("{}Atualmente estamos com 5 generais no jogo, cada qual com sua particularidade{}".format(CORES["cinza"], CORES["limpa"]))
        sleep(1)
        resposta = input("{}Deseja conhecer um pouco sobre suas funcionalidades? (S/N){}".format(CORES["cinza"], CORES["limpa"])+"\n")
        while True:
            if resposta.upper() == 'S':
                print("")
                return True
            elif resposta.upper() == 'N':
                print("")
                return False
            else:
                resposta = input("{}Por gentileza, envie 'S' para sim ou 'N' para nao{}".format(CORES["vermelho"], CORES["limpa"]))

def explicando_generais():
    sleep(1)
    input("{}Decidimos que os generais seriam as únicas peças moveis desse card game.{}".format(CORES["cinza"], CORES["limpa"])+"\n"
          "{}Eles servirão como tanks do game (99 de vida), e serão úteis em diferentes contextos{}".format(CORES["cinza"], CORES["limpa"])+
          "{} e de diferententes formas.{}".format(CORES["cinza"], CORES["limpa"]))
    input("{}Atualmente temos 5 generais, sendo 3 deles personagens históricos e{}".format(CORES["cinza"], CORES["limpa"])+
          "{} dois deles professores.{}".format(CORES["cinza"], CORES["limpa"]))
    input("{}Os 3 generais históricos possuem certos 'buffs' e 'debuffs' diferentes entre si{}".format(CORES["cinza"], CORES["limpa"])+"\n"
          "{}Já os outros dois possuem características compartilhadas.{}".format(CORES["cinza"], CORES["limpa"]))

    input("{}São eles:{}".format(CORES["cinza"], CORES["limpa"]))
    input("{}Alexandre, o Grande e seu poder de ressureição.{}".format(CORES["amarelo"], CORES["limpa"])+"\n"
          "{}Se sua vida chegar a 0 um dano é infligido diretamente na vida do jogador.{}".format(CORES["amarelo"], CORES["limpa"]))
    print()
    sleep(1)
    input("{}Rei Lêonidas.{}".format(CORES["amarelo"], CORES["limpa"])+"\n""{}Dá coragem a um guerreiro aumentando seu alcance e seu dano em batalha.{}".format(CORES["amarelo"], CORES["limpa"])+"\n"
          "{}Se sua vida chegar a zero a coragem dos guerreiros se esvai perdendo vida.{}".format(CORES["amarelo"], CORES["limpa"]))
    print()
    sleep(1)
    input("{}Gengis Khan.{}".format(CORES["amarelo"], CORES["limpa"])+"\n""{}Devido a suas invenções, sua presença em campo de batalha dá a chance de um duplo ataque"
          " dos arqueiros.{}".format(CORES["amarelo"], CORES["limpa"])+"\n""{}Cura a vida do jogador adversário.{}".format(CORES["amarelo"], CORES["limpa"]))
    print()
    sleep(1)
    input("{}Henrique e Iana.{}".format(CORES["amarelo"], CORES["limpa"])+"\n""{}Colocamos os professores de programação como dois dos generais.{}".format(CORES["amarelo"], CORES["limpa"])+"\n"
          "{}Como as cartas são seus alunos, o buff é aplicado nos alunos que pertecerem a turma {}".format(CORES["amarelo"], CORES["limpa"])+
          "{}do professor.{}".format(CORES["amarelo"], CORES["limpa"])+"\n""{}Se a vida chegar a zero o buff é substituido por um debuff de mesmo valor.{}".format(CORES["amarelo"], CORES["limpa"]))
    print()

def MensagemTurno(jogador_turno, lista_nome_jogadores):
    input("{}Agora é o turno do jogador {}: {}{}".format(CORES["amarelo"], jogador_turno+1, lista_nome_jogadores[jogador_turno-1], CORES["limpa"])+'\n')

def mensagem_fim_de_jogo(v1, v2, j1, j2):
    print('{}Fim de Jogo!{}'.format(CORES["verde"], CORES["limpa"]))
    if v1 > 0:
        print('🅟🅐🅡🅐🅑🅔🅝🅢❗')
        print('{}Parabéns ao Jogador 1: {}{}'.format(CORES["verde"], j1, CORES["limpa"]))
    else:
        print('🅟🅐🅡🅐🅑🅔🅝🅢❗')
        print('{}Parabéns ao Jogador 2: {}{}'.format(CORES["verde"], j2, CORES["limpa"]))
    input("{}Obrigado por jogar nosso jogo! Envie qualquer coisa para encerrar{}".format(CORES["verde"], CORES["limpa"]))