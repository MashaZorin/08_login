from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)
accounts = {}
accounts['username'] = 'password'

@app.route('/', methods = ['GET', 'POST'])
def initial():
    if 'username' in session:
        return redirect(url_for('welcome'))
    else:
        return render_template('root.html', message='')

@app.route('/welcome', methods = ['GET', 'POST'])
def welcome():
    if request.method == 'GET':
        username = session['username']
        password = accounts[username]
    else:
        username = request.form['username']
        password = request.form['password']

    if username in accounts and accounts[username] == password:
            session['username'] = username
            return render_template('welcome.html', name=session['username'])
    else:
            return render_template('root.html', message='incorrect, please try again')
    
@app.route('/logout', methods = ['POST'])
def logout():
    session.pop('username')
    return render_template('root.html', message='Logged out!')


if __name__ == '__main__':
    app.debug = True
    app.run()
