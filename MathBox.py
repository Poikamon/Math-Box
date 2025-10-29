#Import

import random
import time

#Função

def MathBox():
    '''Função que escolhe um valor aleatório e compara com um resultado'''
    player = 0
    exvalue = random.randint(-27,27) #Pega um valor possível para a caixa
    print(exvalue)

    MathBox = [] #Lista dos cubos dentro da caixa

    cube1 = input(' numero:')
    a = 0

    match cube1:
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
        case _:
            print("valor inválido")

    MathBox.append(a) #Adiciona valores escolhidos à lista da caixa
    print(a)

    cube2 = input(' numero:')
    b = 0

    match cube2:
        case 'E2801190A503006242D77787':
            b = 1
        case 'E2801190A503006242D77797':
            b = 2
        case 'E2801190A503006242D75217':
            b = 3
        case 'E2801190A503006242D75227':
            b = 4
        case 'E2801190A503006242D75237':
            b = 5
        case 'E2801190A503006242D75247':
            b = 6
        case 'E2801190A503006242D75257':
            b = 7
        case 'E2801190A503006242D75267':
            b = 8
        case 'E2801190A503006242D75287':
            b = 9
        case 'E2801190A503006242D75297':
            b = -1
        case 'E2801190A503006242D752A7':
            b = -2
        case 'E2801190A503006242D752B7':
            b = -3
        case 'E2801190A503006242D77767':
            b = -4
        case 'E2801190A503006242D77757 ':
            b = -5
        case 'E2801190A503006242D77747':
            b = -6
        case 'E2801190A503006242D77727':
            b = -7
        case 'E2801190A503006242D77737':
            b = -8
        case 'E2801190A503006242D77717':
            b = -9
        case _:
            print("valor inválido")
            
    MathBox.append(b) #Adiciona valores escolhidos à lista da caixa
    print(b)

    cube3 = input(' numero:')
    c = 0

    match cube3:
        case 'E2801190A503006242D77787':
            c = 1
        case 'E2801190A503006242D77797':
            c = 2
        case 'E2801190A503006242D75217':
            c = 3
        case 'E2801190A503006242D75227':
            c = 4
        case 'E2801190A503006242D75237':
            c = 5
        case 'E2801190A503006242D75247':
            c = 6
        case 'E2801190A503006242D75257':
            c = 7
        case 'E2801190A503006242D75267':
            c = 8
        case 'E2801190A503006242D75287':
            c = 9
        case 'E2801190A503006242D75297':
            c = -1
        case 'E2801190A503006242D752A7':
            c = -2
        case 'E2801190A503006242D752B7':
            c = -3
        case 'E2801190A503006242D77767':
            c = -4
        case 'E2801190A503006242D77757 ':
            c = -5
        case 'E2801190A503006242D77747':
            c = -6
        case 'E2801190A503006242D77727':
            c = -7
        case 'E2801190A503006242D77737':
            c = -8
        case 'E2801190A503006242D77717':
            c = -9
        case _:
            print("valor inválido")

    MathBox.append(c) #Adiciona valores escolhidos à lista da caixa
    print(c)

    value = sum(MathBox) #soma os valores da caixa

    if value == exvalue:
        print("Resposta correta :)")
        player += 1
    else:
        print("Resposta incorreta :(")  #compara o valor encontrado com o esperado
    print(player)

#Código principal

timer = time.time() + 100 #1 minuto :3

while time.time() < timer:
    MathBox()
print('acabou o tempo!')