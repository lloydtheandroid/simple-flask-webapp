from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/hello')
def hello():
    message = 'Hello World'
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO messages (text) VALUES (?)', (message,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'This is the output from Python: {}'.format(message)})

if __name__ == '__main__':
    app.run(debug=True)
