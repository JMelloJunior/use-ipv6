from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
SECRET_KEY = 'sua-chave-secreta'

@app.route('/api', methods=['GET'])
def api():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Token ausente'}), 401

    try:
        token = token.replace('Bearer ', '')
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        terminal_id = payload.get('terminal_id')
        return jsonify({'message': f'Requisição aceita do terminal {terminal_id}'})
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expirado'}), 403
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Token inválido'}), 403

@app.route('/gerar-token/<terminal_id>', methods=['GET'])
def gerar_token(terminal_id):
    payload = {
        'terminal_id': terminal_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return jsonify({'token': token})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    print(f"Servidor rodando na porta: {port}")
    app.run(host='0.0.0.0', port=port, debug=False)



