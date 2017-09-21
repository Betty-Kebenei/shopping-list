# views.py

from models import User,users,Shopping_list,shopping_list
from flask import render_template, redirect, request,url_for, flash

from app import app

@app.route('/')
def dashboard():
    return render_template("dashboard.html")


@app.route('/signup',methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        first_name = request.form['Firstname']
        last_name = request.form['Lastname']
        user_name = request.form['Username']
        email = request.form['email']
        password = request.form['psw']

        user = User(first_name,last_name,user_name,email,password)
        users.append(user)
        

        return redirect(url_for('signin'))
    return render_template("signup.html")

    
@app.route('/login', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['psw']
        for user in users:
            if email == user.email:
                if password == user.password:
                    
                    return redirect(url_for('dashboard'))
                else:
                    flash('Wrong password!')

            else:
                flash('User not found!')
    return render_template("signin.html")

@app.route('/logout')
def logout():
    return redirect(url_for('signin'))


@app.route('/shop_list',methods=['POST', 'GET'])
def shop_list():
    if request.method == 'POST':
        list_name = request.form['listname']

        s_list = Shopping_list(list_name)
        shopping_list.append(s_list)

        return render_template("dashboard.html", shopping_list = shopping_list)
    return render_template("dashboard.html")

#@app.route('/del_shop_list',methods=['POST', 'GET'])
#def del_shop_list():
    

