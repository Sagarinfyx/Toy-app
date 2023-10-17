from flask import render_template, request, redirect, url_for, flash, session
from app import app
from forms import RegistrationForm, LoginForm
from models import Product, User, CartItem

# Homepage
@app.route('/')
def index():
    products = Product.query.all()  # Query the database to get a list of products
    return render_template('index.html', products=products)

# Product Detail Page
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get(product_id)  # Query the database to get the product details
    return render_template('product.html', product=product)

# Registration Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Process the registration form data, create a new user, and save it to the database
        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Process the login form data and authenticate the user
        flash('Login successful', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


