from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField
from wtforms.validators import InputRequired , Length , EqualTo , ValidationError
from models import User

def invalid_credentials( form , field ):
	""" username and password checker """ 
	username_entered = form.username.data
	password_entered = field.data 
	user_object = User.query.filter_by(username = username_entered).first()
	if user_object is None : 
		raise ValidationError("Username or Password is incorrect !")
	elif password_entered != user_object.password: 
		raise ValidationError("Username or Password is incorrect !")

class RegistrationForm(FlaskForm): 
	username = StringField('username' , validators = [InputRequired(message='User Name Required') , Length(min=4 , max=25 , message="User Name must be between 4 and 25 characters")])
	password = PasswordField('password' , validators = [InputRequired(message='Password Required') , Length(min=4 , max=25 , message="Password must be between 4 and 25 characters")])
	confirm_password = PasswordField('confirm_password' , validators = [InputRequired(message='Confirm Password Required') , EqualTo('password' , message="Passwords must match")])
	submit_button = SubmitField('Create')

	def validate_username(self , username): 
		user_object = User.query.filter_by(username=username.data).first()
		if user_object : 
			raise ValidationError("username already exist , choose another one " )

class LoginForm(FlaskForm): 
	"""Login Form""" 
	username = StringField('username' , validators = [InputRequired(message='username required !')])
	password = PasswordField('password' , validators = [InputRequired(message='password required !') , invalid_credentials])
	submit_button = SubmitField('Login')
