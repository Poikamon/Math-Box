#Import

import random
import threading
#Função

def MathBox():
    '''Função que escolhe um valor aleatório e compara com um resultado'''
    state = False
    player = 0
    while state == False:
        exvalue = random.randint(-45,45) #Pega um valor possível para a caixa
        print(exvalue)

        MathBox = [] #Lista dos cubos dentro da caixa

        state2 = False

        cube = input(' numero:')
        a = 0

        match cube:
            case 'E2801190A503006242D77787':
                a = 1
            case 'E2801190A503006242D77797':
                a = 2
            case 'E2801190A503006242D75217':
                a = 3
            case 'E2801190A503006242D75227':
                a = 4
            case 'E2801190A503006242D75237':
                a = 5
            case 'E2801190A503006242D75247':
                a = 6
            case 'E2801190A503006242D75257':
                a = 7
            case 'E2801190A503006242D75267':
                a = 8
            case 'E2801190A503006242D75287':
                a = 9
            case 'E2801190A503006242D75297':
                a = -1
            case 'E2801190A503006242D752A7':
                a = -2
            case 'E2801190A503006242D752B7':
                a = -3
            case 'E2801190A503006242D77767':
                a = -4
            case 'E2801190A503006242D77757 ':
                a = -5
            case 'E2801190A503006242D77747':
                a = -6
            case 'E2801190A503006242D77727':
                a = -7
            case 'E2801190A503006242D77737':
                a = -8
            case 'E2801190A503006242D77717':
                a = -9

        MathBox.append(a) #Adiciona valores escolhidos à lista da caixa
        value = sum(MathBox) #soma os valores da caixa

        if value == exvalue:
            print("Resposta correta :)")
            player += 1
        else:
            print("Resposta incorreta :(")  #compara o valor encontrado com o esperado
        state = bool(input('Deseja continuar? 1-Sim 0-Não: '))  #Pergunta se o jogador quer continuar

#Código principal

MathBox()
 

