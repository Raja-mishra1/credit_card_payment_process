from flask import Response
def PremiumPaymentGateway(self, *kwargs):
    return Response("OK", status=200)


def ExpensivePaymentGateway(self, *kwargs):
    return Response("OK", status=200)

def CheapPaymentGateway(self, *kwargs):
    return Response("OK", status=200)