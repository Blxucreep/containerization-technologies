# app.py, for docker network practical assignment
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# database connection configuration
db_config = {
    'host': '172.18.0.3', # database container ip
    'database': 'test_db', # database name
    'user': 'postgres', # default postgres user
    'password': 'root', # password
    'port': '5432' # default postgres port
}

# retrieve the data from the database
def get_test_table():
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        # query
        cursor.execute("SELECT * FROM public.test_table;")
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return data
    except Exception as e:
        print(f"Error executing SQL query: {e}")
        return []

# route to display the data
@app.route('/test_table')
def test_table():
    data = get_test_table()
    return jsonify(data)

@app.route('/health')
def health():
    return '200 OK'

if __name__ == '__main__':
    app.run(debug=False, port=8080, host='0.0.0.0')