from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)
accounts = dict()
accounts['username'] = 'password'


@app.route('/', methods = 'POST')
def root():
    return render_template('root.html')

@app.route('/welcome', methods = ['POST'])
def welcome():
    if sessions['username'] in accounts.keys() and accounts[session['username']] == session['password']:
        return render_template('welcome.html', name = session['username'])
    else:
        return render_template('root.html', message = 'Incorrect password-please try again')

@app.route('/logout', methods = ['POST'])
def logout():
    session.pop()
    return render_template('logout.html')

if __name__ == '__main__':
    app.debug = True
app.run()
