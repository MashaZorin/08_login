from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)
accounts = {'username', 'password'}

@app.route('/', methods = ['GET', 'POST'])
def initial():
    if 'username' in session:
        redirect(url_for('welcome'))
    else:
        redirect(url_for('root'))

@app.route('/welcome', methods = ['POST'])
def welcome():
    username = request.form['username']
    password = request.form['username']
    if username in accounts.keys() and account[username] == password:
            session['username'] = username
            redirect(url_for('welcome'))
    else:
            redirect(url_for('error'))
    
@app.route('/logout', methods = ['POST'])
def logout():
    session.pop()
    redirect(url_for('logoutScreen'))

#|==============================================|
def root():
    return render_template('root.html', message='')
def error():
    return render_template('root.html', message='incorrect, please try again')
def welcome():
    return render_template('welcome.html', name=session['username'])
def logoutScreen():
    return render_template('logout.html')
#|==============================================|

if __name__ == '__main__':
    app.debug = True
app.run()
