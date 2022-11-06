from flask import Flask, jsonify
import mysql.connector


app = Flask(__name__)
app.debug = True
       

@app.route('/')
def home():
        return 'API Rest - Olá Inoa'


@app.get('/message')
def get_message():
        conn = mysql.connector.connect(
        user="root",
        password="root",
        host="mysql_db",
        port="3306",
        database="db"
        )
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM messageapi")
        messages = cursor.fetchall()
        messages = dict(messages)
        conn.close()
        
        if len(messages) > 0:
                return jsonify(messages=messages), 200
        return "message not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) # Toda mudança que fizer no código vai rodar automático no site


