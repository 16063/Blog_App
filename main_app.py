from flask import Flask, render_template, url_for
from forms import RegistraionForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '098763f4c0c486c111b00a5cc672c7fc'

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

@app.route("/register")
def register():
    form = RegistraionForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Log In', form=form)

if __name__=='__main__':
    app.run(debug=True) 