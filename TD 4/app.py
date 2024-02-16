# app.py, for docker network practical assignment
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/health')
def health():
    return '200 OK'

if __name__ == '__main__':
    app.run(debug=False, port=8080, host='0.0.0.0')