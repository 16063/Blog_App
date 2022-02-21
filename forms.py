from flask_wtf import FlaskForm
from wtforms import StringFelid, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length 

class RegistraionForm(FlaskForm):
    username = StringFelid('username', validators=[DataRequired(), Length(min=2, max=20)] )
    email = StringFelid('Email', validators=[DataRequired(), Email()] )
    password = PasswordField('Password', validators=[DataRequired()] ) 
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])  
     