from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'thisisuseless'

excuses = [
    "Sorry, the servers are down due to a banana overload.",
    "Oops! The search elf is on a coffee break.",
    "Our database took a nap. Try again never.",
    "404: Grocery sense not found.",
    "Technical difficulties caused by rogue carrots."
]

items = ["Milk", "Bread", "Eggs", "Butter", "Cheese", "Apples"]

@app.route('/', methods=['GET', 'POST'])
def home():
    excuse = ''
    if 'cart' not in session:
        session['cart'] = []
    if request.method == 'POST':
        query = request.form.get('query')
        excuse = random.choice(excuses)
    return render_template('index.html', items=items, excuse=excuse, cart=session['cart'])

@app.route('/add/<item>')
def add_to_cart(item):
    cart = session.get('cart', [])
    cart.append(item)
    session['cart'] = cart
    return redirect(url_for('home'))

@app.route('/remove/<item>')
def remove_from_cart(item):
    cart = session.get('cart', [])
    if item in cart:
        cart.remove(item)
    session['cart'] = cart
    return redirect(url_for('home'))

@app.route('/checkout')
def checkout():
    return "<h1>Checkout failed: Our cart is metaphorical.</h1><a href='/'>Back to shop</a>"

if __name__ == '__main__':
    app.run(debug=True)
