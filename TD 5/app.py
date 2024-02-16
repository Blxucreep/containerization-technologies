# app.py, for docker network practical assignment
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# database connection configuration
db_config = {
    'host': 'db', # db container name
    'database': 'db', # database name
    'user': 'postgres', # default postgres user
    'password': 'root', # password
    'port': '5432' # default postgres port
}

# retrieve the data from the database
def get_students():
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        # query
        cursor.execute("SELECT * FROM students;")
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return data
    except:
        return []

# route to display the data
@app.get('/api/get')
def students():
    data = get_students()
    return jsonify(data)

# insert the data into the database
def insert_student():
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        # query
        cursor.execute("INSERT INTO students (fullname, age) VALUES ('William', 21);")
        connection.commit()

        cursor.close()
        connection.close()

        return 'Data inserted'
    except:
        return 'Error inserting data'

# route to insert the data
@app.post('/api/insert')
def insert():
    data = insert_student()
    return jsonify(data)

@app.route('/health')
def health():
    return '200 OK'

if __name__ == '__main__':
    app.run(debug=False, port=8080, host='0.0.0.0')