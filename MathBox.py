#Import

import random
import serial

#Função

def MathBox():
    '''Função que escolhe um valor aleatório e compara com um resultado'''
    player = 0

    exvalue = random.randint(-45,45) #Pega um valor possível para a caixa

    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = -1
    k = -2
    l = -3
    m = -4
    n = -5
    o = -6
    p = -7
    q = -8
    r = -9

    MathBox = [] #Lista dos cubos dentro da caixa

    MathBox.append() #Adiciona valores escolhidos à lista da caixa

    value = sum(MathBox) #soma os valores da caixa

    if value == exvalue:
        print("Resposta correta :)")
        player += 1
    else:
        print("Resposta incorreta :(")  #compara o valor encontrado com o esperado

#Código principal

Port = serial.Serial(,)
Port.write(MathBox)
