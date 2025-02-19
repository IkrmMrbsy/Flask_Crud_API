from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

#Konfigurasi Database PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2003@localhost:5432/testDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

#Mendefinisikan Model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

#Membuat Table 
with app.app_context():
    db.create_all()

#Endpoint untk Mendapatkan Semua Data
@app.route('/api/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

#Endpoint untk Mendapatkan Data Berdasarkan ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get(item_id)
    if item is None:
        return jsonify({'message': 'Item Not Found'}), 404
    return jsonify({'id': item.id, 'name': item.name})

#Endpoint untk Menambahkan Data Baru
@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.get_json()
    new_item = Item(name=data['name'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'id': new_item.id, 'name': new_item.name}), 201

#Endpoint untk Memperbarui Data 
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get(item_id)
    if item is None:
        return jsonify({'message': 'Item Not Found'}), 404
    data = request.get_json()
    item.name = data['name']
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name})

#Endpoint untk Menghapus Data 
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if item is None:
        return jsonify({'message': 'Item Not Found'}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item Delete'}), 200

if __name__ == '__main__':
    app.run(debug=True)