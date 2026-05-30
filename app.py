from flask import Flask, render_template

app = Flask(__name__)

# Rota principal com dados estáticos para testar a interface
@app.route('/')
def index():
    # Lista simulando dados do banco
    tasks = [
        (1, "Carga SP-RJ", "Eletrônicos", "A Fazer", "Alta"),
        (2, "Entrega Local", "Documentos", "Em Progresso", "Baixa")
    ]
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)