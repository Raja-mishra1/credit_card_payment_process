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
        

    def validate_credit_card_number(self,credit_card_number):
        """[Validates credit card number used in transaction by using Luhn algorithm]

        Returns:
            [bool]: [Returns True if card number is valid otherwise False]
        """
        card_number = list(credit_card_number)
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

    def validate_data(self):
        """[Validates credit card details]

        Returns:
            [Response]: [Returns response if the card details are invalid]
        """
        if self.credit_card_number:
            if type(self.credit_card_number) == str:
                resp = self.validate_credit_card_number(self.credit_card_number)
                if resp == False:
                    return Response("Bad request", status=400)
            else:
                return Response("Bad request", status=400)
        else:
            return Response("Bad request", status=400)
        

        if self.card_holder:
            if  type(self.card_holder) != str:
                return Response("Bad request", status=400)
        else:
            return Response("Bad request", status=400)
            
        if self.expiration_date:
            if type(self.expiration_date) == datetime:
                current_date = datetime.today()
                if self.expiration_date < current_date:
                    return Response("Bad request", status=400)
            else:
                return Response("Bad request", status=400)
        else:
            return Response("Bad request", status=400)
        
        if self.security_code:
            if len(self.security_code) != 3 or type(self.security_code) != str:
                return Response("Bad request", status=400)

        if self.amount:
            if type(self.amount) != float and self.amount >= 0:
                return Response("Bad request", status=400)
        else:
            return Response("Bad request", status=400)


class Payment:
    def __init__(self):
        self.tries = 0

    def process_payment(self,credit_card_number, card_holder, expiration_date, security_code, amount):
        """[Validates credit card related data and passes payment related to payment gateway]

        Args:
            credit_card_number ([str]): [credit card number used in the transaction]
            card_holder ([str]): [Name of credit card holder]
            expiration_date ([datetime]): [Expiration date of credit card]
            security_code ([str]): [Security code of credit card]
            amount ([float]): [Amount involved in the transaction]

        Returns:
            [response]: [Response from payment gateway]
        """
        v = Validate(credit_card_number, card_holder, expiration_date, security_code, amount)
        v.validate_data()
        payment = Payment()
        try:
            if amount <= 20:
                if object:
                    resp = CheapPaymentGateway(credit_card_number, card_holder, expiration_date, security_code, amount)
                    payment.tries +=1
                    return resp

            if amount >= 21 or amount <= 500:
                if object:
                    resp = ExpensivePaymentGateway(credit_card_number, card_holder, expiration_date, security_code, amount)
                    payment.tries +=1
                    return resp
                else:
                    resp = CheapPaymentGateway(credit_card_number, card_holder, expiration_date, security_code, amount)
                    payment.tries +=1

            if amount >= 500:
                if object:
                    resp = PremiumPaymentGateway(credit_card_number, card_holder, expiration_date, security_code, amount)
                    payment.tries +=1
                    return resp

        except:
            return Response("Internal Server error", status=500)



        

    