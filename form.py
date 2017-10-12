from flask import Flask, render_template, request, session, redirect, url_for, flash
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
        return render_template('root.html')

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
    elif username in accounts:
        flash('Incorrect password')
        return redirect(url_for('initial'))
    else:
        flash('Incorrect username')
        return redirect(url_for('initial'))
    
@app.route('/logout', methods = ['POST'])
def logout():
    if 'username' in session:
        flash('Logged out!')
        session.pop('username')
    return redirect(url_for('initial'))


if __name__ == '__main__':
    app.debug = True
    app.run()
