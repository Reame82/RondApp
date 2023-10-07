import json
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

pessoas = []

pessoa1 = {}
pessoa1['codigo'] = 1
pessoa1['nome'] = 'João'
pessoa1['senha'] = 'senha123'
pessoa1['km'] = 0

pessoa2 = {}
pessoa2['codigo'] = 2
pessoa2['nome'] = 'Maria'
pessoa2['senha'] = 'senha456'
pessoa2['km'] = 0

pessoa3 = {}
pessoa3['codigo'] = 3
pessoa3['nome'] = 'Pedro'
pessoa3['senha'] = 'senha789'
pessoa3['km'] = 0

pessoa4 = {}
pessoa4['codigo'] = 4
pessoa4['nome'] = 'Ana'
pessoa4['senha'] = 'senhaabc'
pessoa4['km'] = 0

pessoa5 = {}
pessoa5['codigo'] = 5
pessoa5['nome'] = 'Luísa'
pessoa5['senha'] = 'senhadef'
pessoa5['km'] = 0

pessoa6 = {}
pessoa6['codigo'] = 6
pessoa6['nome'] = 'Rafael'
pessoa6['senha'] = 'senha123'
pessoa6['km'] = 0

pessoa7 = {}
pessoa7['codigo'] = 7
pessoa7['nome'] = 'Camila'
pessoa7['senha'] = 'senha456'
pessoa7['km'] = 0

pessoa8 = {}
pessoa8['codigo'] = 8
pessoa8['nome'] = 'Gustavo'
pessoa8['senha'] = 'senha789'
pessoa8['km'] = 0

pessoa9 = {}
pessoa9['codigo'] = 9
pessoa9['nome'] = 'Julia'
pessoa9['senha'] = 'senhaabc'
pessoa9['km'] = 0

pessoa10 = {}
pessoa10['codigo'] = 10
pessoa10['nome'] = 'Fernando'
pessoa10['senha'] = 'senhadef'
pessoa10['km'] = 0

pessoasCadastradas = [pessoa1, pessoa2, pessoa3, pessoa4, pessoa5, pessoa6, pessoa7, pessoa8, pessoa9, pessoa10]


## Index inicial


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/sucesso', methods=['GET'])
def sucesso():
    return render_template("sucesso.html")


@app.route('/preco', methods=['GET'])
def preco():
    return render_template("preco.html")


@app.route('/cadastro', methods=['GET'])
def cadastro():
    return render_template("cadastro.html")


@app.route('/visualizar', methods=['GET'])
def visualizar():
    return render_template("visualizacao.html", pessoas=pessoasCadastradas)


@app.route('/cadastroRonda', methods=['GET', 'POST'])
def kmrodados():
    if request.method == "GET":

        return render_template("cadastrarRonda.html")
    else:
        cod = int(request.form.get('cod'))
        km = float(request.form.get('km'))  # Converter a quilometragem para float

        for i in range(0, len(pessoasCadastradas)):
            if pessoasCadastradas[i]['codigo'] == cod:
                pessoasCadastradas[i]['km'] += float(km)

        return redirect(url_for('visualizar', mensagem='Cadastrado com sucesso'))


@app.route('/processar_cadastro', methods=['POST'])
def processarCadastro():
    cod = request.form.get('cod')
    nome = request.form.get('nome')
    senha = request.form.get('senha')

    pessoa = {}
    pessoa['codigo'] = cod
    pessoa['nome'] = nome
    pessoa['senha'] = senha
    pessoa['km'] = 0

    pessoasCadastradas.append(pessoa)

    print(pessoasCadastradas)

    return redirect(url_for('sucesso'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
