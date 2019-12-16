from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField
from wtforms.validators import InputRequired , Length , EqualTo


class RegistrationForm(FlaskForm): 
	username = StringField('username' , validators = [InputRequired(message='User Name Required') , Length(min=4 , max=25 , message="User Name must be between 4 and 25 characters")])
	password = PasswordField('password' , validators = [InputRequired(message='Password Required') , Length(min=4 , max=25 , message="Password must be between 4 and 25 characters")])
	confirm_password = PasswordField('confirm_password' , validators = [InputRequired(message='Confirm Password Required') , EqualTo('password' , message="Passwords must match")])
	submit_button = SubmitField('Create')