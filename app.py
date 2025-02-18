from flask import Flask, jsonify, request

app = Flask(__name__)

#Data Dummy 
items = [
    {'id': 1, 'name' : 'ikram'},
    {'id': 2, 'name' : 'Zehan'},
    {'id': 3, 'name' : 'Achmad'}
]

#Endpoint untk Mendapatkan Semua Data
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

#Endpoint untk Mendapatkan Data Berdasarkan ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'message': 'Item Not Found'}), 404
        return jsonify(item)

#Endpoint untk Menambahkan Data Baru
@app.route('/api/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    new_item['id'] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

#Endpoint untk Memperbarui Data 
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'message' : 'Item Not Found'}), 404
    data = request.get_json()
    item.update(data)
    return jsonify(item)

#Endpoint untk Menghapus Data 
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] !=item_id]
    return jsonify({'message': 'Data Delete'}), 200

if __name__ == '__main__':
    app.run(debug=True)