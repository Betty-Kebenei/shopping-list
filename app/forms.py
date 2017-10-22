from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import Length, Email, InputRequired, DataRequired, Regexp, EqualTo, Optional, NumberRange


class LoginForm(Form):
    """Validation form for log in."""

    email = StringField('Email:', validators=[Email(), InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired()])
    submit = SubmitField('Log in')

class SignupForm(Form):
    """Validation form for signing up."""

    firstname = StringField(
        'First Name:', validators=[Length(3, 25),
                                   InputRequired(),
                                   DataRequired(),
                                   Regexp("^[A-Za-z_-]*$",
                                          0,
                                          'Input should only contain letters(\
                                              both uppercase and lowercase) and no spaces')])
    lastname = StringField(
        'Last Name:', validators=[Length(3, 25),
                                  InputRequired(),
                                  DataRequired(),
                                  Regexp("^[A-Za-z_-]*$",
                                         0,
                                         'Input should only contain letters(\
                                             both uppercase and lowercase) and no spaces')])
    username = StringField(
        'User Name:', validators=[Length(3, 25),
                                  InputRequired(),
                                  DataRequired(),
                                  Regexp("^[A-Za-z0-9_-]*$",
                                         0,
                                         'Input should only contain letters(\
                                             both uppercase and lowercase), digits and no spaces')])
    email = StringField('Email:', validators=[Email(), InputRequired()])
    password = PasswordField('Password:', validators=[Length(6, 25), InputRequired(), EqualTo(
        'con_password', message=(u'Your passwords should match.')), Regexp(
            "^(?=.*?[A-Z]).*[0-9]",
            0,
            'Password should contain atleast one digit and atleast one uppercase letter')])
    con_password = PasswordField('Repeat password')
    submit = SubmitField('Sign Up')


class ShoppinglistForm(Form):
    """Validation form for creating lists."""

    listname = StringField(
        'Create a new list:', validators=[Length(3, 25),
                                          InputRequired(),
                                          DataRequired(),
                                          Regexp("^[A-Za-z0-9_-]+( +[A-Za-z0-9_-]+)*$",
                                                 0,
                                                 'Input should only contain letters(\
                                             both uppercase and lowercase), digits and spaces')])
    submit = SubmitField('Create')

class ItemsForm(Form):
    """Validation form for adding items."""

    itemname = StringField(
        'Item Name', validators=[Length(3, 25),
                                 InputRequired(),
                                 DataRequired(),
                                 Regexp("^[A-Za-z0-9_-]+( +[A-Za-z0-9_-]+)*$",
                                        0,
                                        'Input should only contain letters(\
                                             both uppercase and lowercase), digits and spaces')])
    quantity = IntegerField(
        'Quantity', validators=[NumberRange(min=1, max=None, message='%(min)d')])
    price = IntegerField(
        'Price(ksh)', validators=[NumberRange(min=1, max=None, message='%(min)d')])
    submit = SubmitField('Add')

class EditlistForm(Form):
    """Validation form for editing lists."""

    newname = StringField(
        'New listname:', validators=[Length(3, 25),
                                     Optional(strip_whitespace=True),
                                     DataRequired(),
                                     Regexp("^[A-Za-z0-9_-]+( +[A-Za-z0-9_-]+)*$",
                                            0,
                                            'Input should only contain letters(\
                                             both uppercase and lowercase), digits and spaces')])

class EdititemForm(Form):
    """Validation form for editing items."""

    newitemname = StringField(
        'New Item Name', validators=[Length(3, 25),
                                     InputRequired(),
                                     DataRequired(),
                                     Regexp("^[A-Za-z0-9_-]+( +[A-Za-z0-9_-]+)*$",
                                            0,
                                            'Input should only contain letters(\
                                             both uppercase and lowercase), digits and spaces')])
    newquantity = IntegerField(
        'New Quantity', validators=[NumberRange(min=1, max=None, message='%(min)d')])
    newprice = IntegerField(
        'New Price(ksh)', validators=[NumberRange(min=1, max=None, message='%(min)d')])
        