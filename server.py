from flask import Flask, jsonify, request

app = Flask(__name__)

# Iniciando uma variavel global para guardar os dados
ddp = {}

@app.route("/post", methods=["POST"])
def post_data():
    data = request.get_json() # Mudança feita aqui, precisa importar request
    global ddp
    ddp = data
    return jsonify(message="Dados salvos!")

@app.route("/get", methods=["GET"])
def get_data():
    return jsonify(ddp)

if __name__ == '__main__':
    app.run(debug=True)
