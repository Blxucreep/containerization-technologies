from flask import Flask, render_template, redirect, url_for, session

# create the Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'secret_key' # define the secret key

# create the route /main
@app.route('/main')
def home():
    return render_template('main.html')

# create the route /login
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

# create the route /register
@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

# create the route /logout
@app.route('/logout', methods=['GET'])
def logout():
    return redirect(url_for('login'))

# create the route /live
@app.route('/live')
def live():
    return {'status': 'live'}

# run the application
if __name__ == '__main__':
    app.run(debug=True)
