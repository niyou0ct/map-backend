from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import sys

app = Flask(__name__, template_folder='template')
app.secret_key = 'hogehoge'

@app.route('/')
def home():
  if not session.get('logged_in'):
    return render_template('login.html')
  else:
    str_out = ""
    str_out += "<h2>こんにちは</h2>"
    str_out += "Hello Boss!<p />"
    str_out += "<a href='/logout'>Logout</a><br />"

    return str_out

@app.route('/login', methods=['POST'])
def do_admin_login():
  if request.form['username'] == 'scott' \
    and request.form['password'] == 'tiger':
    session['logged_in'] = True
  else:
    flash('wrong password!')
  return home()

@app.route('/logout')
def logout():
  session['logged_in'] = False
  return home()

if __name__ == '__main__':
  app.secret_key = os.urandom(12)
  app.run(debug=True, host='0.0.0.0', port=4000)
