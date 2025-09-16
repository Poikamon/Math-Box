#Import

import random
import serial

#Função

def MathBox():
    '''Função que escolhe um valor aleatório e compara com um resultado'''
    player = 0

    exvalue = random.randint(-45,45) #Pega um valor possível para a caixa

    cube = input()

    a = 0

    match cube:
        case :
            a = 1
        case :
            a = 2
        case :
            a = 3
        case :
            a = 4
        case :
            a = 5
        case :
            a = 6
        case :
            a = 7
        case :
            a = 8
        case :
            a = 9
        case :
            a = -1
        case :
            a = -2
        case :
            a = -3
        case :
            a = -4
        case :
            a = -5
        case :
            a = -6
        case :
            a = -7
        case :
            a = -8
        case :
            a = -9

    MathBox = [] #Lista dos cubos dentro da caixa

    MathBox.append(a) #Adiciona valores escolhidos à lista da caixa

    value = sum(MathBox) #soma os valores da caixa

    if value == exvalue:
        print("Resposta correta :)")
        player += 1
    else:
        print("Resposta incorreta :(")  #compara o valor encontrado com o esperado

#Código principal

Port = serial.Serial(,)
Port.write(MathBox)
