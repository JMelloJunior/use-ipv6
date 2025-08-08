import socket
import threading
from datetime import datetime

HOST = '127.0.0.1'
PORT = 12345

def atender_cliente(conn, addr):
    print(f"[{datetime.now()}] Conectado por {addr}")
    conn.sendall(b'Seu IP foi registrado com sucesso.')
    mensagem = f"Olá {addr[0]}, sua conexão foi registrada às {datetime.now().strftime('%H:%M:%S')}"
    conn.sendall(mensagem.encode('utf-8'))
    conn.close()
    print(f"[{datetime.now()}] Conexão com {addr} encerrada")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor escutando em {HOST}:{PORT}...")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=atender_cliente, args=(conn, addr))
        thread.start()