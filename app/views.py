# views.py
from app.models import User, users, Shopping_list, shopping_list, Shopping_items
from flask import session, render_template, redirect, request, url_for, flash
from app import app
from app.forms import LoginForm, SignupForm, S_listForm, ItemsForm, EditlistForm, EdititemForm

def login_session(user):
    """Enabling users should have session."""

    session["email"] = user.email
    session["list_id"] = user.email.list_id
    session["logged_in"] = True
    return redirect(url_for('dashboard'))

def verify_login_session():
    """Ensuring users should have session."""

    if not session["logged_in"]:
        return redirect(url_for('signin'))

@app.route('/dashboard')
def dashboard():
    """Directs user to the dashboard."""
     
    if session["logged_in"] is True:
        form = S_listForm()
        user_shopping_list = []  # container for user shopping list
        for shl in shopping_list:
            if shl.created_by == session.get('email'):  # check owner
                user_shopping_list.append(shl)  # append if true

        return render_template("dashboard.html", form=form, shopping_list=user_shopping_list)
    else:
        return redirect(url_for('signin'))     

@app.route('/signup',methods=['POST', 'GET'])
def signup():
    """Enabling users to sign up."""

    form = SignupForm()
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        con_password = form.con_password.data
        if password == con_password:
            user = User(firstname, lastname, username, email, password)
            users.append(user)
            return redirect(url_for('signin'))
        else:
            flash('Your password is not equal to your confirm password.')
    return render_template("signup.html", form=form)

@app.route('/login', methods=['POST', 'GET'])
def signin():
    """Enabling users to sign in."""

    form = LoginForm()
    if request.method == 'POST':
        email = form.email.data
        password = form.password.data
        for user in users:
            if email == user.email:
                if password == user.password:
                    session["logged_in"] = True
                    session["email"] = email
                    return redirect(url_for('dashboard'))
                else:
                    flash('Wrong password!')
            else:
                flash('User not found!')
        return redirect(url_for('dashboard'))
    return render_template("signin.html", form=form)

@app.route('/logout')
def logout():
    """Enabling users to log out."""

    session["logged_in"] = False
    return redirect(url_for('signin'))

@app.route('/shop_list', methods=['POST', 'GET'])
def shop_list():
    """Enabling users to create shopping lists."""

    form = S_listForm()
    if form.validate_on_submit():
        listname = form.listname.data
        s_list = Shopping_list(listname, created_by=session.get('email'))  # pass the owner
        shopping_list.append(s_list)  # remove owner and just append created list only
    return redirect(url_for('dashboard'))

@app.route('/del_list/<list_id>', methods=['GET'])
def del_list(list_id):
    """Enabling users to delete shopping lists."""

    for items in shopping_list:
        if items['lst'].list_id == int(list_id):
            shopping_list.remove(items)
            return redirect(url_for("dashboard"))
    return redirect(url_for("dashboard"))

@app.route('/edit_list/<list_id>', methods=['POST'])
def edit_list(list_id):
    """Enabling users to update shopping lists."""

    form = EditlistForm(request.form)
    new_name = form.newname.data
    for items in shopping_list:
        if items['lst'].list_id == int(list_id):
            items['lst'].listname = new_name
            return redirect(url_for("dashboard"))
    return render_template("dashboard.html", form=form)

@app.route('/view_lists', methods=['POST', 'GET'])
def view_lists():
    """Enabliging users to view shopping list."""

    form = ItemsForm()
    if request.method == 'POST':
        return redirect(url_for('shop_list'))
    return render_template("shoppingitems.html", form=form)

@app.route('/view_items/<list_id>', methods=['POST', 'GET'])
def view_items(list_id):
    """Enabling users to view their shopping items."""

    form = ItemsForm()
    for items in shopping_list:  # loop through the shopping list
        if items.list_id == int(list_id):
            session["list_id"] = list_id

    return render_template("shoppingitems.html", form=form, shopping_list=shopping_list)  # pass the shopping list to the template

@app.route('/shop_item', methods=['POST', 'GET'])
def shop_item():
    """Enabling users to add shopping items to their shopping lists."""

    form = ItemsForm()
    if request.method == 'POST':
        itemname = form.itemname.data
        quantity = form.quantity.data
        price = form.price.data
        item = Shopping_items(itemname, quantity, price)
        for shopping in shopping_list:
            shopping.shopping_items.append(item)

        # i interchanged `return` position, please check your previous code
        return redirect(url_for('shop_item'))
    return render_template("shoppingitems.html", form=form, shopping_list=shopping_list)


@app.route('/edit_item/<item_id>', methods=['POST'])
def edit_item(item_id):
    """Enabling users to update their shopping items."""

    form = EdititemForm(request.form)
    newitemname = form.newitemname.data
    newquantity = form.newquantity.data
    newprice = form.newprice.data
    for shopping in shopping_list:
        if shopping.shopping_items.item_id == int(item_id):
            shopping.shopping_items.itemname = newitemname
            shopping.shopping_items.quantity = newquantity
            shopping.shopping_items.price = newprice
            return redirect(url_for("dashboard"))
    return render_template("dashboard.html", form=form)
