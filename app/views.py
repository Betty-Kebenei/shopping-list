# views.py
import string
from models import User,users,Shopping_list,shopping_list,Shopping_items,shopping_items
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

        user = User(first_name, last_name, user_name, email,password)
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
        listname = request.form['listname'].strip()
        if len(listname) != 0:
            s_list = Shopping_list(listname)
            shopping_list.append(s_list)   
        else:
            raise TypeError('No empty strings allowed.')

        return render_template("dashboard.html", shopping_list = shopping_list)
    return render_template("dashboard.html")

@app.route('/shop_list/<list_id>/del',methods=['DELETE'])
def del_shop_list(list_id):
    shop_list=listname.query.get(list_id)
    if shop_list is None:
        return jsonify(
            status='error', message='shopping list with id {}'.format(list_id))
    shopping_list.delete(shop_list)
    return jsonify(status='ok')

    # for items in shopping_items:
    #     name = request.form['item.listname']
    #     if name in shopping_list:
    #         shopping_list.remove(name)

    #     return redirect(url_for('dashboard'))
    # return render_template("signin.html")

@app.route('/view_lists',methods=['POST', 'GET'])
def view_listss():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template("shoppingitems.html")

@app.route('/view_items',methods=['POST', 'GET'])
def view_items():
    if request.method == 'POST':
        return redirect(url_for('shop_item'))
    return render_template("dashboard.html")

@app.route('/shop_item',methods=['POST', 'GET'])
def shop_item():
    if request.method == 'POST':
        itemname = request.form['itemname']
        quantity= request.form['quantity']
        price = request.form['price']

        item = Shopping_items(itemname,quantity,price)
        shopping_items.append(item)

        return render_template("shoppingitems.html", shopping_items = shopping_items)
    return render_template("shoppingitems.html")
    

