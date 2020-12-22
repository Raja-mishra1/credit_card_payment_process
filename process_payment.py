from datetime import datetime
from flask import Response
from payment_gateway import PremiumPaymentGateway,CheapPaymentGateway,ExpensivePaymentGateway


class Validate:
    def __init__(self,credit_card_number, card_holder, expiration_date, security_code, amount):
        self.credit_card_number = credit_card_number
        self.card_holder = card_holder
        self.expiration_date = expiration_date
        self.security_code = security_code
        self.amount = amount

    def validate_credit_card_number(self, card_number):
        card_number = list(card_number)
        check_digit = card_number.pop()
        card_number.reverse()
        processed_digits = []

        for index, digit in enumerate(card_number):
            if index % 2 == 0:
                doubled_digit = int(digit) * 2
            
                if doubled_digit > 9:
                    doubled_digit = doubled_digit - 9

                processed_digits.append(doubled_digit)
            else:
                processed_digits.append(int(digit))

        total = int(check_digit) + sum(processed_digits)
        if total % 10 == 0:
            return True
        else:
            return False

    def validate_data(self,credit_card_number,card_holder,expiration_date,security_code,amount):
        if credit_card_number:
            if type(credit_card_number) == str:
                resp = self.validate_credit_card_number(credit_card_number)
                if resp == False:
                    return Response("Bad request", status=400)
            else:
                return Response("Bad request", status=400)
        else:
            return Response("Bad request", status=400)
        

        if card_holder:
            if  type(card_holder) != str:
                return Response("Bad request", status=400)
        else:
            return Response("Bad request", status=400)
            
        if expiration_date:
            if type(expiration_date) == datetime:
                current_date = datetime.today()
                if expiration_date < current_date:
                    return Response("Bad request", status=400)
            else:
                return Response("Bad request", status=400)
        else:
            return Response("Bad request", status=400)
        
        if security_code:
            if len(security_code) != 3 or type(security_code) != str:
                return Response("Bad request", status=400)

        if amount:
            if type(amount) != float and amount >= 0:
                return Response("Bad request", status=400)
        else:
            return Response("Bad request", status=400)



def process_payment(credit_card_number, card_holder, expiration_date, security_code, amount):
    v = Validate(credit_card_number, card_holder, expiration_date, security_code, amount)
    v.validate_data(credit_card_number, card_holder, expiration_date, security_code, amount)
    try:
        if amount <= 20:
            resp = CheapPaymentGateway(credit_card_number, card_holder, expiration_date, security_code, amount)
            return resp
        if amount >= 21 or amount <= 500:
            resp = ExpensivePaymentGateway(credit_card_number, card_holder, expiration_date, security_code, amount)
            return resp
        if amount >= 500:
            resp = PremiumPaymentGateway(credit_card_number, card_holder, expiration_date, security_code, amount)
            return resp

    except:
        return Response("Internal Server error", status=500)
    

    