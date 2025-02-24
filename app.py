from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

# Function to calculate total price
def calculate_total_price(price, quantity):
    return price * quantity

# Function to load existing cart data
def load_cart():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save cart data
def save_cart(cart_data):
    with open(DATA_FILE, "w") as file:
        json.dump(cart_data, file, indent=4)

@app.route("/", methods=["GET", "POST"])
def index():
    total_price = None
    cart_items = []

    if request.method == "POST":
        total_price = 0  # Initialize total price
        cart_items = []   # Initialize cart items list

        for i in range(3):  # Loop for 3 items
            price = float(request.form.get(f"price{i}", 0))
            quantity = int(request.form.get(f"quantity{i}", 0))
            total = calculate_total_price(price, quantity)

            cart_items.append({"price": price, "quantity": quantity, "total": total})
            total_price += total

        # Load existing cart and add new items
        cart_data = load_cart()
        cart_data.extend(cart_items)
        save_cart(cart_data)  # Save updated cart

    return render_template("index.html", total_price=total_price, cart_items=load_cart())

@app.route("/cart", methods=["GET"])
def get_cart():
    return jsonify(load_cart())  # API to get cart data in JSON format

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)