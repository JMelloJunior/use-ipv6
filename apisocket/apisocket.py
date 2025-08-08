from flask import Flask, jsonify, request
from datetime import datetime
import socket

app = Flask(__name__)

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

@app.route("/info", methods=["GET"])
def info():
    ip_cliente = request.remote_addr
    tipo = tipo_ip(ip_cliente)
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    resposta = {
        "tipo_ip": tipo,
        "endereco": ip_cliente,
        "data_hora": agora
    }
    return jsonify(resposta)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)