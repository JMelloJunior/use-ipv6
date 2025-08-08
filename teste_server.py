import socket
import threading
import json
from datetime import datetime

HOST = '127.0.0.1'
PORT = 5000

def tipo_ip(endereco):
    try:
        socket.inet_pton(socket.AF_INET, endereco)
        return "IPv4"
    except OSError:
        try:
            socket.inet_pton(socket.AF_INET6, endereco)
            return "IPv6"
        except OSError:
            return "Desconhecido"

def handle_client(conn, addr):
    with conn:
        ip_cliente = addr[0]
        tipo = tipo_ip(ip_cliente)
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resposta = {
            "tipo_ip": tipo,
            "endereco": ip_cliente,
            "data_hora": agora
        }
        conn.sendall((json.dumps(resposta) + '\n').encode())
        print(f"[Servidor] Atendido: {ip_cliente} ({tipo}) às {agora}", flush=True)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("[Servidor] Aguardando conexões...", flush=True)
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()