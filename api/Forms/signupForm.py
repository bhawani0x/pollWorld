from flask_wtf import FlaskForm
from api.app import app
from wtforms import StringField, PasswordField, DateField, SelectField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.csrf import CSRFProtect
import email_validator

# csrf = CSRFProtect()


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    username = StringField('Username', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    mobile_number = StringField('Mobile Number', validators=[DataRequired(), Length(max=15)])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
                         validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])


csrf.init_app(app)
