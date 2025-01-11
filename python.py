from flask import Flask, render_template_string

app = Flask(__name__)

# Sample data (could be dynamic)
products = [
    {"name": "T-shirt", "price": 499, "description": "Comfortable cotton t-shirt.", "image": "https://via.placeholder.com/200x200?text=T-shirt"},
    {"name": "Jeans", "price": 999, "description": "Stylish blue jeans.", "image": "https://via.placeholder.com/200x200?text=Jeans"},
    {"name": "Shoes", "price": 1299, "description": "Durable running shoes.", "image": "https://via.placeholder.com/200x200?text=Shoes"},
]

# HTML template as a string
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Myntra Clone</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background-color: #e60000;
            color: white;
            padding: 10px 0;
            text-align: center;
        }
        h1 {
            margin: 0;
        }
        .products {
            padding: 20px;
        }
        .product-list {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
        }
        .product {
            background-color: white;
            padding: 15px;
            margin: 10px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 200px;
        }
        .product img {
            width: 100%;
            height: auto;
            border-radius: 8px;
        }
        button {
            background-color: #e60000;
            color: white;
            padding: 10px;
            border: none;
            cursor: pointer;
        }
        footer {
            text-align: center;
            margin-top: 20px;
        }
        footer a {
            color: #e60000;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Myntra Clone</h1>
    </header>

    <section class="products">
        <h2>Featured Products</h2>
        <div class="product-list">
            {% for product in products %}
                <div class="product">
                    <img src="{{ product.image }}" alt="{{ product.name }}">
                    <h3>{{ product.name }}</h3>
                    <p>₹{{ product.price }}</p>
                    <p>{{ product.description }}</p>
                    <button>Add to Cart</button>
                </div>
            {% endfor %}
        </div>
    </section>

    <footer>
        <p>&copy; 2025 Myntra Clone</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def index():
    # Render the HTML template and pass the products list
    return render_template_string(html_code, products=products)

if __name__ == '__main__':
    app.run(debug=True)

