import random
#--------------------------------------------- JOGO DE ADVINHAÇÃO -----------------------------------------------------#
#Funções
def linha(x):
    print(x*"-")

def jogar():
#----------------------------------------------Programa Principal------------------------------------------------------#
    numero_secreto = random.randrange (1,101)
    print("      Bem vindos ao jogo de adivinhação")
    linha(45)
    print("Nesse jogo você deve acertar o número secreto")
    linha(45)
    total_tentativas = 0
    pontos = 1000

    print('Escolha o nível: ')
    print('(0) fácil, (1) médio, (2) difícil')

    nivel = int(input('Escolha o nível que deseja jogar: '))

    if (nivel == 0):
        total_tentativas = 20

    elif (nivel == 1):
        total_tentativas = 10

    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa:{} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Digite um número entre 1 e 100: ")
            continue
        #------------------------------------------------Variáveis-------------------------------------------------------------#
        chute = int(chute_str)
        acertou = numero_secreto == chute
        menor = chute < numero_secreto
        maior = chute > numero_secreto
        #-----------------------------------------------Condicionais-----------------------------------------------------------#
        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break

        else:
            if(menor):
                print("Esse número é menor que o número secreto!")

            elif (maior):
                print("Esse número é maior que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos



    print("Fim do programa")
if (__name__ =="__main__" ):
    jogar()
