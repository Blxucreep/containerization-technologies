from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# database connection configuration
db_config = {
    'host': 'db', # db container name
    'database': 'db', # database name
    'user': 'postgres', # default postgres user
    'password': 'root', # password
    'port': '3000' # default postgres port
}

def get_messages(sender, receiver):
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        # query
        cursor.execute(f"SELECT * FROM messages WHERE sender = '{sender}' AND receiver = '{receiver}';")
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return data
    except:
        return []

def insert_message(sender, receiver, message):
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        # query
        cursor.execute(f"INSERT INTO messages (sender, receiver, message) VALUES ('{sender}', '{receiver}', '{message}');")
        connection.commit()

        cursor.close()
        connection.close()

        return 'Data inserted'
    except:
        return 'Error inserting data'
    
@app.get('/api/get/<sender>/<receiver>')
def messages(sender, receiver):
    data = get_messages(sender, receiver)
    return jsonify(data)

@app.post('/api/insert/<sender>/<receiver>/<message>')
def insert(sender, receiver, message):
    data = insert_message(sender, receiver, message)
    return jsonify(data)

@app.route('/health')
def health():
    return '200 OK'

if __name__ == '__main__':
    app.run(debug=False, port=5001, host='0.0.0.0')