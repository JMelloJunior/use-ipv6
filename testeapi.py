from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/info", methods=["GET"])
def info():
    return jsonify({"mensagem": "API funcionando!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)