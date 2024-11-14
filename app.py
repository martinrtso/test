from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)


db_config = {
    'host': os.environ.get('DB_HOST'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'database': os.environ.get('DB_NAME')
}

@app.route('/')
def get_materia():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM materia")
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        
        result = [{'id': row[0], 'nombre': row[1]} for row in rows]
        return jsonify(result)
    except mysql.connector.Error as err:
        return str(err), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)