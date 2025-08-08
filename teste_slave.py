import socket

print("[Cliente] Script iniciado.", flush=True)

HOST = '127.0.0.1'
PORT = 5000

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("[Cliente] Tentando conectar...", flush=True)
        s.connect((HOST, PORT))
        print("[Cliente] Conectado ao servidor.", flush=True)
        resposta = s.recv(1024)
        print("[Cliente] Resposta recebida:", resposta.decode(), flush=True)
except Exception as e:
    print("[Cliente] Erro:", e, flush=True)