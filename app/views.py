# views.py
from app.models import User, users, Shopping_list, shopping_list, Shopping_items, shopping_items
from flask import render_template, redirect, request, url_for, flash
from app import app
from app.forms import LoginForm, SignupForm, S_listForm, ItemsForm

@app.route('/')
def dashboard():
    form=S_listForm()
    return render_template("dashboard.html", form=form)

@app.route('/signup',methods=['POST', 'GET'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user = User(firstname, lastname, username, email, password)
        users.append(user)
        return redirect(url_for('signin'))
    return render_template("signup.html", form=form)
   
@app.route('/login', methods=['POST', 'GET'])
def signin():
    form = LoginForm()
    if request.method == 'POST':
        email = form.email.data
        password = form.password.data
        for user in users:
            if email == user.email:
                if password == user.password:
                    return redirect(url_for('dashboard'))
                else:
                    flash('Wrong password!')
            else:
                flash('User not found!')
        return redirect(url_for('dashboard'))
    return render_template("signin.html", form=form)

@app.route('/logout')
def logout():
    return redirect(url_for('signin'))

@app.route('/shop_list',methods=['POST', 'GET'])
def shop_list():
    form = S_listForm()
    if form.validate_on_submit():
        listname = form.listname.data
        s_list = Shopping_list(listname)
        shopping_list.append(s_list) 
        return render_template("dashboard.html", form=form, shopping_list=shopping_list)
    return redirect(url_for('dashboard'))

@app.route('/shop_list/del/<list_id>')
def del_shop_list(list_id):
    if list_id in shopping_list:
        listname = shopping_list.remove
        Shopping_list.remove_list()
        return redirect(url_for('dashboard'))
    return render_template("dashboard.html")

@app.route('/view_lists', methods=['POST', 'GET'])
def view_lists():
    form=ItemsForm()
    if request.method == 'POST':
        return redirect(url_for('shop_list'))
    return render_template("shoppingitems.html", form=form)

@app.route('/view_items', methods=['POST', 'GET'])
def view_items():
    form=ItemsForm()
    return render_template("shoppingitems.html", form=form)

@app.route('/shop_item', methods=['POST', 'GET'])
def shop_item():
    form = ItemsForm()
    if request.method == 'POST':
        itemname = form.itemname.data
        quantity = form.quantity.data
        price = form.price.data
        item = Shopping_items(itemname, quantity, price)
        shopping_items.append(item)
        return render_template("shoppingitems.html",form=form, shopping_items=shopping_items)
    return redirect(url_for('shop_item'))