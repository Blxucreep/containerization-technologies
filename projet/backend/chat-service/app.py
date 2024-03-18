from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# create the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('MESSAGE_DATABASE_URL', 'postgresql://normaluser:user@chat-service-db:5432/postgres-db') # PostgreSQL database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

# initialize CORS
CORS(app)

# initialize SQLAlchemy
db = SQLAlchemy(app)

# create a Message model
class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Text, nullable=False)
    receiver = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)

# create the route /send_message
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    sender = data.get('sender')
    receiver = data.get('receiver')
    content = data.get('content')

    if not all([sender, receiver, content]):
        return jsonify({"warning": "sender, receiver, and message content are required"}), 400

    message = Message(sender=sender, receiver=receiver, content=content)
    db.session.add(message)
    db.session.commit()

    return jsonify({"msg": "message sent successfully"}), 201

# create the route /get_messages/<username>
@app.route('/get_messages/<username>', methods=['GET'])
def get_messages(username):
    sent_messages = Message.query.filter_by(sender=username).all()
    received_messages = Message.query.filter_by(receiver=username).all()

    sent_messages = [{'id': message.id, 'sender': message.sender, 'receiver': message.receiver, 'content': message.content} for message in sent_messages]
    received_messages = [{'id': message.id, 'sender': message.sender, 'receiver': message.receiver, 'content': message.content} for message in received_messages]

    return jsonify({"sent_messages": sent_messages, "received_messages": received_messages}), 200

# live route
@app.route('/live', methods=['GET'])
def live():
    return jsonify({"status": "live"}), 200

# run the application
if __name__ == '__main__':
    with app.app_context():
        print("creating message database tables...")
        db.create_all()
        print("message database tables created.")
    app.run(debug=True)
