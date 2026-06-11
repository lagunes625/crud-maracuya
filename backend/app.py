from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

enfermedades = []

@app.route('/')
def inicio():
    return "Servidor funcionando"

@app.route('/enfermedades', methods=['GET'])
def listar():
    return jsonify(enfermedades)

@app.route('/enfermedades', methods=['POST'])
def agregar():

    datos = request.json

    enfermedad = {
        "id": datos["id"],
        "nombre": datos["nombre"],
        "descripcion": datos["descripcion"]
    }

    enfermedades.append(enfermedad)

    return jsonify({
        "mensaje":"Enfermedad agregada"
    })

@app.route('/enfermedades/<int:id>', methods=['GET'])
def leer(id):

    for enfermedad in enfermedades:

        if int(enfermedad["id"]) == id:

            return jsonify(enfermedad)

    return jsonify({
        "mensaje":"Enfermedad no encontrada"
    }), 404

@app.route('/enfermedades/<int:id>', methods=['PUT'])
def modificar(id):

    datos = request.json

    for enfermedad in enfermedades:

        if int(enfermedad["id"]) == id:

            enfermedad["nombre"] = datos["nombre"]
            enfermedad["descripcion"] = datos["descripcion"]

            return jsonify({
                "mensaje":"Enfermedad modificada"
            })

    return jsonify({
        "mensaje":"Enfermedad no encontrada"
    }), 404

@app.route('/enfermedades/<int:id>', methods=['DELETE'])
def eliminar(id):

    for enfermedad in enfermedades:

        if int(enfermedad["id"]) == id:

            enfermedades.remove(enfermedad)

            return jsonify({
                "mensaje":"Enfermedad eliminada"
            })

    return jsonify({
        "mensaje":"Enfermedad no encontrada"
    }), 404

if __name__ == '__main__':
    app.run(debug=True)