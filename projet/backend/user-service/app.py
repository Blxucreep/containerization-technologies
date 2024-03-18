from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token
from flask_migrate import Migrate
from flask_cors import CORS
import bcrypt
import os

# create the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://normaluser:user@user-service-db:5432/postgres-db') # PostgreSQL database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'warum')

# initialize CORS
CORS(app)

# initialize SQLAlchemy
db = SQLAlchemy(app)
# initialize JWT
jwt = JWTManager(app)
# initialize Migrate
migrate = Migrate(app, db)

# create a User model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# create the route /signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"warning": "username and password are required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"warning": "username already exists"}), 409

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(username=username, password=hashed_password.decode('utf-8'))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "user created successfully"}), 201

# create the route /login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"warning": "bad username or password"}), 401

# create the route /get_users
@app.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    users = [{'id': user.id, 'username': user.username} for user in users]

    return jsonify({"users": users}), 200

# live route
@app.route('/live', methods=['GET'])
def live():
    return jsonify({"status": "live"}), 200

# run the application
if __name__ == '__main__':
    with app.app_context():
        print("creating database tables...")
        db.create_all()
        print("database tables created.")
    app.run(debug=True)
