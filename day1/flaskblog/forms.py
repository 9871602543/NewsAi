from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired



class RegistrationForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username exist use another name.')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Chalaki nahi mittar ye id pehle use kr chuka h')    


class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember me')
    submit=SubmitField('Log In')


class UpdateAccountForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Update')

    
    def validate_username(self,username):
        if username.data!=current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username exist use another name.')

    def validate_email(self,email):
        if email.data!=current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Chalaki nahi mittar ye id pehle use kr chuka h')  
            
class RequestResetForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    submit=SubmitField('Request Reset')
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Bhai pehle account to bnale! Ye email hae hi nhi DB mei faltu mei resource waste kia.') 


class ResetPasswordForm(FlaskForm):
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    
    submit=SubmitField('Reset Password')            




class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')    