from flask import Blueprint, jsonify, request
from app import db
from app.models.item import Item

item_bp = Blueprint('item_bp', __name__)

# Endpoint untuk mendapatkan semua item
@item_bp.route('/', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

# Endpoint untuk mendapatkan item berdasarkan ID
@item_bp.route('/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({'message': 'Item Not Found'}), 404
    return jsonify({'id': item.id, 'name': item.name})

# Endpoint untuk menambahkan item baru
@item_bp.route('/', methods=['POST'])
def add_item():
    data = request.get_json()
    new_item = Item(name=data['name'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'id': new_item.id, 'name': new_item.name}), 201

# Endpoint untuk memperbarui item
@item_bp.route('/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({'message': 'Item Not Found'}), 404

    data = request.get_json()
    item.name = data['name']
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name})

# Endpoint untuk menghapus item
@item_bp.route('/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({'message': 'Item Not Found'}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item Deleted'}), 200
