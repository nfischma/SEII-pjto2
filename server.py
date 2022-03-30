import socket
import threading
import time

#define o ip do servidor coo endereco IP do HOST
SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER_IP, PORT)
#define o formato de comunicação como utf-8
FORMATO = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

conexoes = []
mensagens = []
estados_leds = ["0","0"]

def enviar_estados(conexao):
    #Essa função manda a mensagem i da lista mensagens para uma conexao
    print(f"[ENVIANDO] Enviando mensagens para {conexao['addr']}")
    mensagem_de_envio = "leds=" + estados_leds[0] + ";" + estados_leds[1]
    conexao['conn'].send(mensagem_de_envio.encode())
    time.sleep(0.2)
    print('fim enviar estados')

"""
1 vez que o cliente entrar, vai mandar o nome:
nome=.....
E as mensagens vem:
msg=
"""

def handle_clientes(conn, addr):
    #Essa função recebe o endereço, a conexão e o nome de um cliente
    #e envia uma mensagem individual para ele
    #ou envia todas as mensagens para os clientes
    print(f"[NOVA CONEXAO] Um novo usuario se conectou pelo endereço {addr}")
    global conexoes
    global mensagens
    recebido = False
    while(not recebido):
        msg = conn.recv(1024).decode(FORMATO)
        if(msg):
            recebido = True
            if(msg.startswith("state_request")):
                mapa_da_conexao = {
                    "conn": conn,
                    "addr": addr,
                    "last": 1
                }
                conexoes.append(mapa_da_conexao)
                enviar_estados(mapa_da_conexao)



def start():
    #abre o server e establece a conexão como thread
    print("[INICIANDO] Iniciando Socket")
    server.listen()    
    conn, addr = server.accept()
    while(True):
        thread = threading.Thread(target=handle_clientes, args=(conn, addr))
        thread.start()
        thread.join()
        print("[ENVIADO]")

start()