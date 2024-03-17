from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'une_cle_secrete_tres_secure'  # Une clé secrète est nécessaire pour la session

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)  # Notez que j'ai changé ceci pour password_hash

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@app.before_first_request
def create_tables():
    db.create_all()

#region login
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        
        if user is not None and user.check_password(password):
            # L'utilisateur existe et le mot de passe est correct
            return redirect(url_for('main'))
        else:
            # L'email n'existe pas ou le mot de passe est incorrect
            flash('Email or password is incorrect.', 'error')  # Le deuxième argument est facultatif et représente une catégorie
            return redirect(url_for('login'))  # Redirection vers la page de connexion

    return render_template('login.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('registration.html')
#endregion

#region register

@app.route('/register', methods=['POST'])
def register_post():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    existing_user = User.query.filter_by(username=username).first()
    if existing_user is None:
        new_user = User(username=username, email=email)
        new_user.set_password(password)  # Ici, nous hashons le mot de passe
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        return "Un compte avec ce nom d'utilisateur existe déjà."
#endregion

#region main
@app.route('/logout', methods=['GET'])
def logout():
    # Votre code pour effacer la session
    session.clear()
    return redirect(url_for('login'))

#search users 
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')  # Obtenez la requête de recherche de l'URL
    if query:
        # Utilisez '%' comme jokers pour la recherche SQL LIKE
        users = User.query.filter(User.username.like('%' + query + '%')).all()
        user_list = [{'id': user.id, 'username': user.username} for user in users]
    else:
        user_list = []

    return {'users': user_list}  # Retournez la liste d'utilisateurs en JSON

@app.route('/chat/<username>')
def chat(username):
    # Vous devrez ajouter une logique pour vérifier si l'utilisateur actuel a
    # le droit de discuter avec l'utilisateur `username`.
    # Ensuite, récupérez les messages du chat ou tout autre information nécessaire.
    
    return render_template('chat.html', username=username)

#endregion

@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
