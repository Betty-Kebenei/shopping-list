from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import Length, Email, InputRequired, DataRequired, Regexp


class LoginForm(Form):
    """Validation form for log in."""

    email = StringField('Email:', validators=[Email(), InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired()])
    submit = SubmitField('Log in')

class SignupForm(Form):
    """Validation form for signing up."""

    firstname = StringField(
        'First Name:', validators=[Length(3, 50),
                                   InputRequired(),
                                   DataRequired(),
                                   Regexp("^[A-Za-z_-]+(\s+[A-Za-z_-]+)*$",
                                          0,
                                          'Input should contain [A-Za-z_-] spaces')])
    lastname = StringField(
        'Last Name:', validators=[Length(3, 50),
                                  InputRequired(),
                                  DataRequired(),
                                  Regexp("^[A-Za-z_-]+(\s+[A-Za-z_-]+)*$",
                                         0,
                                         'Input should contain [A-Za-z_-] spaces')])                                               
    username = StringField(
        'User Name:', validators=[Length(3, 50),
                                  InputRequired(),
                                  DataRequired(),
                                  Regexp("^[A-Za-z0-9_-]+(\s+[A-Za-z0-9_-]+)*$",
                                         0,
                                         'Input should contain [A-Za-z0-9_-] spaces')])
    email = StringField('Email:', validators=[Email(), InputRequired()])
    password = PasswordField('Password:', validators=[Length(6, 50), InputRequired()])
    con_password = PasswordField('Confirm Password:', validators=[Length(6, 50), InputRequired()])
    submit = SubmitField('Sign Up')


class S_listForm(Form):
    """Validation form for creating lists."""

    listname = StringField(
        'Create a new list:', validators=[Length(3, 50),
                                          InputRequired(),
                                          DataRequired(),
                                          Regexp("^[A-Za-z0-9_-]+(\s+[A-Za-z0-9_-]+)*$",
                                                 0,
                                                 'Input should contain [A-Za-z0-9_-] spaces')])
    submit = SubmitField('Create')

class ItemsForm(Form):
    """Validation form for adding items."""

    itemname = StringField(
        'Item Name', validators=[Length(3, 50),
                                 InputRequired(),
                                 DataRequired(),
                                 Regexp("^[A-Za-z0-9_-]+(\s+[A-Za-z0-9_-]+)*$",
                                        0,
                                        'Input should contain [A-Za-z0-9_-] spaces')])
    quantity = IntegerField(
        'Quantity', validators=[Length(1, 50),
                                InputRequired(),
                                DataRequired(),
                                Regexp("^[0-9]+(\s+[0-9]+)*$",
                                       0,
                                       'Input should contain [0-9] spaces')])
    price = IntegerField(
        'Price(ksh)', validators=[Length(1, 50),
                                  InputRequired(),
                                  DataRequired(),
                                  Regexp("^[0-9]+(\s+[0-9]+)*$",
                                         0,
                                         'Input should contain [0-9] spaces')])
    submit = SubmitField('Add')

class EditlistForm(Form):
    """Validation form for editing lists."""

    newname = StringField(
        'New listname:', validators=[Length(3, 50),
                                     InputRequired(),
                                     DataRequired(),
                                     Regexp("^[A-Za-z0-9_-]+(\s+[A-Za-z0-9_-]+)*$",
                                            0,
                                            'Input should contain [A-Za-z0-9_-] spaces')])
                                            
class EdititemForm(Form):
    """Validation form for editing items."""

    newitemname = StringField(
        'New Item Name', validators=[Length(3, 50),
                                     InputRequired(),
                                     DataRequired(),
                                     Regexp("^[A-Za-z0-9_-]+(\s+[A-Za-z0-9_-]+)*$",
                                            0,
                                            'Input should contain [A-Za-z0-9_-] spaces')])
    newquantity = IntegerField(
        'New Quantity', validators=[Length(1, 50),
                                    InputRequired(),
                                    DataRequired(),
                                    Regexp("^[0-9]+(\s+[0-9]+)*$",
                                           0,
                                           'Input should contain [0-9] spaces')])
    newprice = IntegerField(
        'New Price(ksh)', validators=[Length(1, 50),
                                      InputRequired(),
                                      DataRequired(),
                                      Regexp("^[0-9]+(\s+[0-9]+)*$",
                                             0,
                                             'Input should contain [0-9] spaces')])
