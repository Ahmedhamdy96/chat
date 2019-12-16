from flask import Flask , render_template
from wtform_fields import * 
from models import * 

# configure app 
app = Flask( __name__)
app.secret_key = 'top secret'

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kykezvnkvxmhpl:323481a7dc7a496db337c41ff1542a9d81aa25b4f7e23f33402611a9c6a11cc2@ec2-174-129-255-35.compute-1.amazonaws.com:5432/d4ve4a3kl1pgck'
db = SQLAlchemy(app)

@app.route("/" , methods = [ 'GET' , 'POST'])
def index():
	reg_form = RegistrationForm()
	
	if reg_form.validate_on_submit() : 
		username = reg_form.username.data 
		password = reg_form.password.data 

		# add the user to database 
		user = User(username=username , password=password)
		db.session.add(user)
		db.session.commit()
		return "Inserted in Database Successfully !"
	return render_template('index.html' , form=reg_form)

if __name__ == '__main__': 
    app.run(debug=True)