# app.py, for docker network practical assignment
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# database connection configuration
db_config = {
    'host': '127.0.0.1', # host name
    'database': 'db', # database name
    'user': 'postgres', # default postgres user
    'password': 'root', # password
    'port': '5432' # default postgres port
}

# retrieve the data from the database
def get_students():
    try:
        connection = psycopg2.connect(**db_config)
        print('Connection:', connection)
        cursor = connection.cursor()

        # query
        cursor.execute("SELECT * FROM students;")
        data = cursor.fetchall()
        print(data)

        cursor.close()
        connection.close()

        return data
    except Exception as e:
        print(f"Error executing SQL query: {e}")
        return []

# insert the data into the database
def insert_student():
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        # query
        cursor.execute("INSERT INTO students (name, age) VALUES ('William', 21);")
        connection.commit()

        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error executing SQL query: {e}")

# route to display the data
@app.route('/api/get')
def students():
    data = get_students()
    return jsonify(data)

# route to insert the data
@app.route('/api/insert')
def insert():
    insert_student()
    return 'DATA INSERTED'

@app.route('/health')
def health():
    return '200 OK'

if __name__ == '__main__':
    app.run(debug=False, port=8080, host='0.0.0.0')