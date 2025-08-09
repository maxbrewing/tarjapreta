from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def painel():
    membros = [
        {'nome': 'Carlos Silva', 'email': 'carlos@email.com'},
        {'nome': 'Joana Souza', 'email': 'joana@email.com'}
    ]

    eventos = [
        {'nome': 'Encontro Nacional', 'data': datetime(2025, 8, 20)},
        {'nome': 'Motociata Brasília', 'data': datetime(2025, 9, 5)}
    ]

    aniversariantes = [
        {'nome': 'Rafael Motta'}
    ]

    return render_template(
        'painel.html',
        membros=membros,
        eventos=eventos,
        aniversariantes=aniversariantes
    )

if __name__ == '__main__':
    app.run(debug=True)