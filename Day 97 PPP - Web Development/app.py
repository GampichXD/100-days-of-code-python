# Professional Portfolio Project - Web Development
# An Online Shop
# Author : Abraham
from flask import Flask, render_template, redirect, url_for, session, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, Product
import stripe_keys
import stripe

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', [])
    cart.append(product_id)
    session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart_items = Product.query.filter(Product.id.in_(session.get('cart', []))).all()
    total = sum(item.price for item in cart_items)
    return render_template('cart.html', items=cart_items, total=total)

@app.route('/checkout', methods=['POST'])
def checkout():
    cart_items = Product.query.filter(Product.id.in_(session.get('cart', []))).all()
    line_items = [{
        'price_data': {
            'currency': 'usd',
            'product_data': {'name': item.name},
            'unit_amount': item.price,
        },
        'quantity': 1
    } for item in cart_items]

    session_stripe = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=stripe_keys.YOUR_DOMAIN + '/success',
        cancel_url=stripe_keys.YOUR_DOMAIN + '/cart'
    )

    return redirect(session_stripe.url, code=303)

@app.route('/success')
def success():
    session['cart'] = []
    return render_template('success.html')
