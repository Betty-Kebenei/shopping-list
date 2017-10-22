# views.py

from flask import session, render_template, redirect, request, url_for, flash
from app import app
from app.models import User, users, Shopping_list, shopping_list, Shopping_items
from app.forms import LoginForm, SignupForm, ShoppinglistForm, ItemsForm, EditlistForm, EdititemForm

# Creating sessions.
def login_session(user):
    """Enabling users should have session."""

    session["email"] = user.email
    session["list_id"] = user.email.list_id
    session["logged_in"] = True
    session.clear()
    return redirect(url_for('dashboard'))

# Views on class User.
@app.route('/signup',methods=['POST', 'GET'])
def signup():
    """Enabling users to sign up."""

    form = SignupForm()
    if request.method == 'POST' and form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        if users:
            for user in users:
                if user.email == email:
                    flash("User with the email exist.")
                else:
                    user = User(firstname, lastname, username, email, password)
                    users.append(user)
                    return redirect(url_for('signin'))
        else:
            user = User(firstname, lastname, username, email, password)
            users.append(user)
            return redirect(url_for('signin'))
    return render_template("signup.html", form=form)

@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def signin():
    """Enabling users to sign in."""

    form = LoginForm()
    if request.method == 'POST':
        email = form.email.data
        password = form.password.data
        if users:
            for user in users:
                if user.email == email:
                    if user.password == password:
                        session["logged_in"] = True
                        session["email"] = user.email
                        return redirect(url_for('dashboard'))
                    else:
                        flash('Wrong password!')
                else:
                    flash('User not found!')
        else:
            flash('User not found.')
    return render_template("signin.html", form=form)

@app.route('/logout')
def logout():
    """Enabling users to log out."""

    session["logged_in"] = False
    return redirect(url_for('signin'))

# Views on class Shopping_list
@app.route('/dashboard')
def dashboard():
    """Directs user to the dashboard."""
    
    if not session["logged_in"]:
        return redirect(url_for('signin'))
    else:
        form = ShoppinglistForm()
        return render_template("dashboard.html", form=form, shopping_list=shopping_list)

@app.route('/shop_list', methods=['POST', 'GET'])
def shop_list():
    """Enabling users to create shopping lists."""

    form = ShoppinglistForm()
    if form.validate_on_submit():
        listname = form.listname.data
        created_by = session.get('email')
        s_list = Shopping_list(listname, created_by)
        if shopping_list:
            for shoppinglist in shopping_list:
                if not shoppinglist.listname == listname:
                    shopping_list.append(s_list)      
        else:
            shopping_list.append(s_list)
        return render_template("dashboard.html", form=form, shopping_list=shopping_list)
    return redirect(url_for('dashboard'))

@app.route('/del_list/<list_id>', methods=['POST'])
def del_list(list_id):
    """Enabling users to delete shopping lists."""

    for items in shopping_list:
        if items.list_id == list_id:
            shopping_list.remove(items)
            return redirect(url_for("dashboard"))
    return redirect(url_for("dashboard"))

@app.route('/edit_list/<list_id>', methods=['POST'])
def edit_list(list_id):
    """Enabling users to update shopping lists."""

    form = EditlistForm(request.form)
    new_name = form.newname
    for items in shopping_list:
        if items.list_id == list_id:
            items.listname = new_name
            return redirect(url_for("dashboard"))
    return redirect(url_for("dashboard"))

@app.route('/view_lists', methods=['POST', 'GET'])
def view_lists():
    """Enabliging users to view shopping list."""

    form = ItemsForm()
    if request.method == 'POST':
        return redirect(url_for('shop_list'))
    return render_template("shoppingitems.html", form=form)

# Views on class Shopping_items
@app.route('/items/<list_id>', methods=['POST', 'GET'])
def items(list_id):
    """Enabling users to place the list_id into session so that an item will be added to a specific list."""

    form = ItemsForm()
    session["list_id"] = list_id
    return render_template("shoppingitems.html", form=form)

@app.route('/shopping_items')
def shopping_items():
    """Directs user to the shopping items page."""
    
    if not session["logged_in"]:
        return redirect(url_for('signin'))
    else:
        form = ItemsForm()
        return render_template("shoppingitems.html", form=form, shopping_list=shopping_list)

@app.route('/add_item', methods=['POST', 'GET'])
def add_item():
    """Enabling users to add shopping items to their shopping lists."""

    form = ItemsForm()
    if request.method == 'POST' and form.validate_on_submit():
        itemname = form.itemname.data
        quantity = form.quantity.data
        price = form.price.data
        item = Shopping_items(itemname, quantity, price) 
        for shopping in shopping_list:
            if shopping.list_id == session['list_id']:
                if shopping.shopping_items:
                    for items in shopping.shopping_items:
                        if not items.itemname == itemname:
                            shopping.shopping_items.append(item)
                else: 
                    shopping.shopping_items.append(item)
                return render_template("shoppingitems.html", form=form, shopping_list=shopping_list)
    return redirect(url_for('shopping_items'))

@app.route('/view_items/<list_id>', methods=['POST', 'GET'])
def view_items(list_id):
    """Enabling users to view shopping items in a shopping list."""

    session["list_id"] = list_id
    form = ItemsForm()
    for shopping in shopping_list:
        if shopping.list_id == list_id:
            return render_template("shoppingitems.html", form=form, shopping_list=shopping_list)
    return redirect(url_for('dashboard'))

@app.route('/edit_item/<item_id>', methods=['POST'])
def edit_item(item_id):
    """Enabling users to update their shopping items."""

    form = EdititemForm(request.form)
    newitemname = form.newitemname.data
    newquantity = form.newquantity.data
    newprice = form.newprice.data
    for shopping in shopping_list:
        for i in shopping.shopping_items:
            if i.item_id == int(item_id):
                i.itemname = newitemname
                i.quantity = newquantity
                i.price = newprice
                return redirect(url_for("shopping_items"))
    return render_template("shoppingitems.html", form=form)

@app.route('/del_item/<item_id>', methods=['POST'])
def del_item(item_id):
    """Enabling users to delete a shopping item in a shopping list."""

    for shopping in shopping_list:
        for i in shopping.shopping_items:
            if i.item_id == int(item_id):
                shopping.shopping_items.remove(i)
                return redirect(url_for("shopping_items"))
    return render_template("shoppingitems.html")

