from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

# Página inicial para listar tarefas
@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# Adiciona uma nova tarefa
@app.route('/add', methods=['POST'])
def add_task():
    task_description = request.form['description']
    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (description) VALUES (?)', (task_description,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Deleta uma tarefa
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Cria o banco de dados e a tabela, se não existirem
    conn = get_db_connection()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL
    )
    ''')
    conn.close()

    app.run(host='0.0.0.0', port=8080)
