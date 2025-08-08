import socket

HOST = '0.0.0.0'  # Escuta em todas as interfaces
PORT = 12345      # Porta de escuta

# Cria o socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Servidor escutando na porta {PORT}...")

while True:
    conn, addr = server_socket.accept()
    client_ip = addr[0]
    print(f"Conexão recebida de: {client_ip}")

    conn.sendall(b"Seu IP foi registrado com sucesso.\n")
    conn.close()

