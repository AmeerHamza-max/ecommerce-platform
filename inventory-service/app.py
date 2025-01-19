from flask import Flask, jsonify, request

app = Flask(__name__)

inventory = {}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Inventory Service"}), 200

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory), 200

@app.route('/inventory', methods=['POST'])
def add_inventory():
    data = request.json
    inventory[data["product_id"]] = data["quantity"]
    return jsonify({"message": "Inventory updated", "inventory": inventory}), 201

@app.route('/inventory/<int:product_id>', methods=['PUT'])
def update_inventory(product_id):
    if product_id in inventory:
        inventory[product_id] = request.json["quantity"]
        return jsonify({"message": "Inventory updated", "inventory": inventory}), 200
    return jsonify({"error": "Product not found in inventory"}), 404

@app.route('/inventory/<int:product_id>', methods=['DELETE'])
def delete_inventory(product_id):
    if product_id in inventory:
        del inventory[product_id]
        return jsonify({"message": "Inventory removed"}), 200
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
