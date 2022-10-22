from ast import Delete
from crypt import methods
from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O senhor dos Anéis - A sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    { 
        'id': 2,
        'título': 'James Clear',
        'autor': 'Hábitos Atômicos'
    },
    { 
        'id': 3,
        'título': 'É Assim que Acaba',
        'autor': 'Collen Hoover'
    },
    ]

# Consultar (todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)


# Consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_id(id):
    for livro in livros:
        livro.get('id')
        return jsonify(livro)


# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    request.get_json()
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    nome_livro = request.get_json()
    livros.append(incluir_novo_livro)

    return jsonify(livros)

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

        return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)