#Import

import streamlit as st
import random
import time

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#Variáveis 

player = 0
placeholder = st.empty()

#Função

def MathBox():
    '''Função que escolhe um valor aleatório e compara com um resultado'''
    exvalue = random.randint(-27,27) #Pega um valor possível para a caixa
    placeholder.markdown(
        f"""
        <div class='bloco-valor'>
            {exvalue}
        </div>
        """,
        unsafe_allow_html=True
    )
    time.sleep(2)

    MathBox = [] #Lista dos cubos dentro da caixa

    placeholder.markdown("<div class='titulo'>Primeiro número:</div>", unsafe_allow_html=True)
    
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
    placeholder.markdown("<div class='titulo'>Segundo número:</div>", unsafe_allow_html=True)
    
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
    placeholder.markdown("<div class='titulo'>Terceiro número:</div>", unsafe_allow_html=True)   
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
        placeholder.markdown("<div class='correto'>Resposta correta :)</div>", unsafe_allow_html=True)
        player += 1
    else:
        placeholder.markdown("<div class='errado'>Resposta incorreta :(</div>", unsafe_allow_html=True)

#Código principal

placeholder.markdown(
    """
    <h1 class='titulo-principal'>
        Aperte o botão e teste sua habilidade matemática!
    </h1>
    """,
    unsafe_allow_html=True
)

op = input()

if op == 's':
    timer = time.time() + 100 #1 minuto :3

    while time.time() < timer:
        MathBox()
        time.sleep(2)
    print('acabou o tempo!')
    player = 0
# O código abaixo é para rodar no Raspberry Pi com o botão físico
        
#Código principal
        # Configurar a numeração dos pinos
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

# Definir o número do pino do botão
#botao_pin = 3
# Configurar o pino do botão como entrada com pull-up interno (o botão é conectado entre o pino e o terra)
#GPIO.setup(botao_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#timer = time.time() + 120

#try:
    #while True:
        # Ler o estado do botão
        # Se o botão estiver pressionado, a leitura será baixa (LOW)
        #if GPIO.input(botao_pin) == GPIO.LOW:
            #while time.time()<timer:
                #MathBox()
#except KeyboardInterrupt:
    #print("Programa encerrado.")
#finally:
    #GPIO.cleanup()



