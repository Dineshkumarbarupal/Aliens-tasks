from flask import Flask, render_template, request, jsonify, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Database setup
def init_db():
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    
    # Create tables
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            email TEXT
        )
    ''')
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE, 
            price REAL,
            description TEXT,
            image_url TEXT
        )
    ''')
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            total_price REAL,
            status TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    ''')
    
    # Pehle check karein products already hain ya nahi
    c.execute('SELECT COUNT(*) FROM products')
    product_count = c.fetchone()[0]
    
    # Agar products nahi hain tabhi insert karein
    if product_count == 0:
        products = [
            ('Laptop', 999.99, 'High-performance laptop', '/static/laptop.jpg'),
            ('Smartphone', 699.99, 'Latest smartphone', '/static/phone.jpg'),
            ('Headphones', 199.99, 'Noise-cancelling headphones', '/static/headphones.jpg')
        ]
        
        c.executemany('INSERT INTO products (name, price, description, image_url) VALUES (?, ?, ?, ?)', products)
        print("Sample products inserted")
    else:
        print(f"Database already has {product_count} products")
    
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/products')
def get_products():
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    c.execute('SELECT * FROM products')
    products = c.fetchall()
    conn.close()
    
    product_list = []
    for product in products:
        product_list.append({
            'id': product[0],
            'name': product[1],
            'price': product[2],
            'description': product[3],
            'image_url': product[4]
        })
    
    return jsonify(product_list)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Simple authentication (in real app, use proper auth)
    if username == 'testuser' and password == 'password':
        session['user'] = username
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

@app.route('/api/order', methods=['POST'])
def create_order():
    if 'user' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    
    # Get product price
    c.execute('SELECT price FROM products WHERE id = ?', (product_id,))
    product = c.fetchone()
    
    if not product:
        return jsonify({'success': False, 'message': 'Product not found'}), 404
    
    total_price = product[0] * quantity
    
    # Create order
    c.execute('''
        INSERT INTO orders (user_id, product_id, quantity, total_price, status)
        VALUES (?, ?, ?, ?, ?)
    ''', (1, product_id, quantity, total_price, 'pending'))
    
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'message': 'Order created', 'total': total_price})

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)