from flask import Flask, render_template, request, redirect, url_for, session
from data.content_page import data_content as dc
from flask_session import Session
from private.get_data import getDataLogin as gdl
from private.login_handle import loginTools
from private.key_storage import storage_private as sp
import os

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'your_secret_key'  # Ganti dengan secret key Anda
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/user')
def mainUser():
    #Return 
    return render_template(
        'User.html',
        data = dc.user_content_data()
        )
    
# Login System:
@app.route('/login', methods = ['GET','POST'])
def loginPage():
    # Get Data
    userkey = sp.userkey()
    passkey = sp.passkey()
    data = gdl.putData('username', 'password')
    if loginTools.loginHandle(data, userkey, passkey):
        session['logged_in'] = True  # Menyimpan status login di session
        session['username'] = data[0]  # Menyimpan username di session
        return redirect(url_for('admin'))
    else:
        print("Login gagal!")
    
    
    # Return
    return render_template(
        'LoginPage.html',
        data = dc.login_content_data()
        )
    
@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        return redirect(url_for('loginPage'))
    return render_template(
        'admin.html',
        data = dc.admin_content_data(),
        username=session['username']
        )

@app.route('/logout')
def logout():
    # Menghapus status login dari session
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('loginPage'))