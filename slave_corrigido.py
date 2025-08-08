import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Servidor escutando...")

    conn, addr = s.accept()
    with conn:
        ip_cliente = addr[0]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Registro em tempo real
        registro = f"{timestamp} - IP conectado: {ip_cliente}"
        print(registro)  # Mostra no terminal

        # Salva em arquivo
        with open("ips_registrados.txt", "a") as f:
            f.write(registro + "\n")

        # Envia confirmação ao cliente
        conn.sendall(f"Seu IP ({ip_cliente}) foi registrado às {timestamp}".encode('utf-8'))