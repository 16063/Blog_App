from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint
from forms import RegistraionForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '098763f4c0c486c111b00a5cc672c7fc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), unique=True, nullable=False)
  posts = db.relationship('Post', backref='author', lazy=True)
  
  def __repr__(self):
    return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    
    

posts = [
    
    {
        'author' : 'Mark Glasse ',
        'title' : 'Blog Post 1',
        'content' : 'first post content',
        'date_posted' : 'Febuary 14, 2022'
    },
    
    {
        'author' : 'Ryan Clifford ',
        'title' : '15 regis lane',
        'content' : '147.117.41.147',
        'date_posted' : 'Febuary 14, 2022'
    }
    
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistraionForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login" , methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password': 
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your username and password', 'danger')
    return render_template('login.html', title='Log In', form=form)

if __name__=='__main__':
    app.run(debug=True) 