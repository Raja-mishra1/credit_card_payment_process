from process_payment import Payment
from datetime import datetime
credit_card_number = "354673100235957"
card_holder = "RAm"
expiration_date = datetime.strptime("20201231",'%Y%m%d')
security_code = "CVV"
amount = 100.70
pay = Payment()
resp = pay.process_payment(credit_card_number,card_holder,expiration_date,security_code,amount)
print("response --->",resp)