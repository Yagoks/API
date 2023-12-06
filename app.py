from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Configuração da conexão com o banco de dados
conn = psycopg2.connect(
    dbname='vzwktuqx',
    user='vzwktuqx',
    password='eTQoYre_S0pEfOs4E0ytjNpGFLiBTRmk',
    host='silly.db.elephantsql.com',
    port='5432'
)

# Consultar(todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    cur = conn.cursor()
    cur.execute('SELECT * FROM livros')
    livros = cur.fetchall()
    cur.close()
    # Convertendo os resultados para um formato JSON
    livros_json = [{'id': livro[0], 'título': livro[1], 'autor': livro[2]} for livro in livros]
    return jsonify(livros_json)

# Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    cur = conn.cursor()
    cur.execute('SELECT * FROM livros WHERE id = %s', (id,))
    livro = cur.fetchone()
    cur.close()
    if livro:
        livro_json = {'id': livro[0], 'título': livro[1], 'autor': livro[2]}
        return jsonify(livro_json)
    else:
        return jsonify({'mensagem': 'Livro não encontrado'}), 404

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
