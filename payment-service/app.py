from flask import Flask, jsonify, request

app = Flask(__name__)

payments = []

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Payment Service"}), 200

@app.route('/payments', methods=['GET'])
def get_payments():
    return jsonify(payments), 200

@app.route('/payments', methods=['POST'])
def process_payment():
    payment = request.json
    payments.append(payment)
    return jsonify({"message": "Payment processed", "payment": payment}), 200

@app.route('/payments/<int:payment_id>', methods=['PUT'])
def update_payment(payment_id):
    for payment in payments:
        if payment["id"] == payment_id:
            payment.update(request.json)
            return jsonify({"message": "Payment updated", "payment": payment}), 200
    return jsonify({"error": "Payment not found"}), 404

@app.route('/payments/<int:payment_id>', methods=['DELETE'])
def refund_payment(payment_id):
    global payments
    payments = [p for p in payments if p["id"] != payment_id]
    return jsonify({"message": "Payment refunded"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
