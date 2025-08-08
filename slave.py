import socket

HOST = '127.0.0.1'
PORT = 12345

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        print("Conectando ao servidor...")
        s.connect((HOST, PORT))
        resposta = s.recv(1024)
        print("Mensagem recebida do servidor:", resposta.decode('utf-8'))
except socket.timeout:
    print("Tempo de espera excedido. Nenhuma resposta recebida.")
except ConnectionRefusedError:
    print("Não foi possível conectar ao servidor. Ele está rodando?")