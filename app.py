from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("username")
        
        # Replace these values with your desired login credentials
        if username == 'admin' and password == 'password':
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Try again.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

#sign up form
@app.route('/signup',methods=['GET', 'POST'])
def signup():
     return render_template('signup.html')
    
# Feedback form
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    name = request.form.get("name")
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    return redirect(url_for('home'))

# Shopping Cart (for a logged-in user)
@app.route('/cart')
def view_cart():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        cart_items = CartItem.query.filter_by(user_id=user.id).all()
        return render_template('cart.html', cart_items=cart_items, user=user)
    else:
        flash('Please log in to view your shopping cart.', 'warning')
        return redirect(url_for('login'))

# Checkout (for a logged-in user)
@app.route('/checkout')
def checkout():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        cart_items = CartItem.query.filter_by(user_id=user.id).all()
        total_cost = sum(item.product.price for item in cart_items)
        return render_template('checkout.html', cart_items=cart_items, user=user, total_cost=total_cost)
    else:
        flash('Please log in to proceed to checkout.', 'warning')
        return redirect(url_for('login'))

#forgot_paswwword
@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        # Generate secure token and send password reset email
        return 'Password reset email sent'
    return render_template('forgot_password.html')  # Provide a form for email input

if __name__ == '__main__':
    app.run(debug=True)