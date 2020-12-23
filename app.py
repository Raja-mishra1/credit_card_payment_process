from flask import Flask, jsonify, request
from config import FLASK_SERVER, FLASK_PORT, FLASK_LOGGING
from process_payment import Payment
app = Flask(__name__)


@app.route("/api/v1/payments/", methods=["POST"])
def member_create():
    credit_card_number = request.json["CreditCardNumber"]
    card_holder = request.json["CardHolder"]
    expiration_date = request.json["ExpirationDate"]
    security_code = request.json["SecurityCode"]
    amount = request.json["Amount"]
    pay = Payment()
    response = pay.process_payment(credit_card_number,card_holder,expiration_date,security_code,amount)
    return response


if __name__ == "__main__":
    app.run(host=FLASK_SERVER, port=FLASK_PORT, debug=False, threaded=True)