import socket
import threading
import time

import pygame

import numpy as np
import matplotlib.pyplot as plt

#criação janela
pygame.display.set_caption("Simulação LEDS")
screen = pygame.display.set_mode((1620,960))

#criação background
background = pygame.image.load('imagens_leds/background.png')


running = True


PORT = 5050
FORMATO = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname()) #"192.168.0.109"
ADDR = (SERVER, PORT)

clk = time.time()
#abre o socket e se conecta no endereço definido
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

estados = ["0","0"]

def receber_estado():
    global estados
    #esssa funcao trata a mensagem enviada separando ela pelo '='
    recebido = False
    while(not recebido):
        msg = client.recv(1024).decode()
        if(msg):
            recebido = True
        msg = msg.replace('leds=', '')
        estados = msg.split(";")
    
    time.sleep(0.2)
    

def enviar(mensagem):
    #enssa função envia a mensagem no formato utf-8
    client.send(mensagem.encode(FORMATO))


def state_request():
    enviar("state_request")
    time.sleep(0.1)

def pedir_estado():
    #O thread 1 mostra as mensagens enviadas
    thread1 = threading.Thread(target=receber_estado)
    #O thread 2 pede o nome e a mensagem do utilizados para mandar os dois
    thread2 = threading.Thread(target=state_request())
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


while running:
    
    for event in pygame.event.get():
        #fecha a simulação se fechar a janela
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    if time.time()-clk > 0.5:
        pedir_estado()

  
    #mostrar o background
    screen.blit(background, (0, 0))

    #atualizar LEDS
    if estados[0] == "0":
        led1 = pygame.image.load("imagens_leds/desligada.jpg")
    else:
        led1 = pygame.image.load("imagens_leds/ligada.jpg")
    if estados[1] == "0":
        led2 = pygame.image.load("imagens_leds/desligada.jpg")
    else:
        led2 = pygame.image.load("imagens_leds/ligada.jpg")
    
    screen.blit(led1,(0,0))
    screen.blit(led2, (1000,0))

    #atualizar a tela
    pygame.display.flip()
      