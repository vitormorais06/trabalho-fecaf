from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__) 

#banco dea dadis em sqlite para facilitar a integração do projeto
def init_db():
    """Cria o banco de dados e a tabela de tarefas caso não existam."""
    conn = sqlite3.connect('logistics.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  title TEXT NOT NULL,
                  description TEXT, 
                  status TEXT NOT NULL, 
                  priority TEXT NOT NULL)''')
    conn.commit() 
    conn.close()  




#pagina principal
@app.route('/')
def index():
    """Busca as tarefas cadastradas e renderiza a tela inicial."""
    conn = sqlite3.connect('logistics.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)



#criar tarefa
@app.route('/add', methods=['POST'])
def add_task():
    """Recebe os dados do formulário HTML e insere no banco de dados."""
    # Capturando os valores digitados no formulário
    title = request.form['title']
    description = request.form['description']
    status = request.form['status']
    priority = request.form['priority']
    
    conn = sqlite3.connect('logistics.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (title, description, status, priority) VALUES (?, ?, ?, ?)",
              (title, description, status, priority))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))



#deletar a tarefa
@app.route('/delete/<int:id>')
def delete_task(id):
    """Deleta uma tarefa específica baseada no ID recebido pela URL."""
    conn = sqlite3.connect('logistics.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True)