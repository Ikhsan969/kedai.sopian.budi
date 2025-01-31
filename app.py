from flask import Flask, render_template, request, jsonify, session, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Kunci untuk session

@app.route('/')
def index():
    menu_items = [
        {"id": 1, "name": "Americano", "price": 4.00, "image": url_for('static', filename='images/americano.jpg')},
        {"id": 2, "name": "Iced Affogato", "price": 5.50, "image": url_for('static', filename='images/affogato.jpg')},
        {"id": 3, "name": "Capuchino Iced", "price": 3.50, "image": url_for('static', filename='images/capucino.jpg')},
        {"id": 4, "name": "Espresso", "price": 3.00, "image": url_for('static', filename='images/esspreso.jpg')},
        {"id": 5, "name": "Kopi Gula Aren", "price": 3.07, "image": url_for('static', filename='images/gula aren.jpg')},
        {"id": 6, "name": "Hazelnut Coffee", "price": 3.56, "image": url_for('static', filename='images/hazlenut.jpg')},
        {"id": 7, "name": "Coffee Latte", "price": 3.45, "image": url_for('static', filename='images/cofee latte.jpg')},
        {"id": 8, "name": "Caramel Macchiato", "price": 3.45, "image": url_for('static', filename='images/caramel machiato.jpg')},
        {"id": 9, "name": "Kopi Susu Tubruk", "price": 3.77, "image": url_for('static', filename='images/kopi tubruk.jpg')},
        {"id": 10, "name": "Mocachino Iced", "price": 3.77, "image": url_for('static', filename='images/mochacino.jpg')}
    ]
    return render_template('index.html', menu=menu_items)

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    return render_template('cart.html', cart=cart_items)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.json
    item_id = int(data.get('id'))

    # Definisikan ulang menu_items di dalam fungsi ini
    menu_items = [
        {"id": 1, "name": "Americano", "price": 4.00, "image": url_for('static', filename='images/americano.jpg')},
        {"id": 2, "name": "Iced Affogato", "price": 5.50, "image": url_for('static', filename='images/affogato.jpg')},
        {"id": 3, "name": "Capuchino Iced", "price": 3.50, "image": url_for('static', filename='images/capucino.jpg')},
        {"id": 4, "name": "Espresso", "price": 3.00, "image": url_for('static', filename='images/esspreso.jpg')},
        {"id": 5, "name": "Kopi Gula Aren", "price": 3.07, "image": url_for('static', filename='images/gula aren.jpg')},
        {"id": 6, "name": "Hazelnut Coffee", "price": 3.56, "image": url_for('static', filename='images/hazlenut.jpg')},
        {"id": 7, "name": "Coffee Latte", "price": 3.45, "image": url_for('static', filename='images/cofee latte.jpg')},
        {"id": 8, "name": "Caramel Macchiato", "price": 3.45, "image": url_for('static', filename='images/caramel machiato.jpg')},
        {"id": 9, "name": "Kopi Susu Tubruk", "price": 3.77, "image": url_for('static', filename='images/kopi tubruk.jpg')},
        {"id": 10, "name": "Mocachino Iced", "price": 3.77, "image": url_for('static', filename='images/mochacino.jpg')}
    ]

    # Cari item berdasarkan ID
    item = next((i for i in menu_items if i['id'] == item_id), None)
    
    if not item:
        return jsonify({"message": "Item not found"}), 404

    # Ambil keranjang dari session, jika belum ada buat array kosong
    cart = session.get('cart', [])
    cart.append(item)
    session['cart'] = cart
    session.modified = True  # Pastikan perubahan disimpan
    
    return jsonify({"message": "Item added to cart", "cart": cart})

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    data = request.json
    item_id = int(data.get('id'))

    cart = session.get('cart', [])
    cart = [item for item in cart if item['id'] != item_id]
    
    session['cart'] = cart
    session.modified = True

    return jsonify({"success": True, "cart": cart})

if __name__ == '__main__':
    app.run(debug=True)
