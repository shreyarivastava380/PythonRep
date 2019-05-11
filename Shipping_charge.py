purchaseValue=False
orderValue=float(input(' Please enter the total value of your purchase'))
if orderValue<50 :
    purchaseValue=True
if purchaseValue :
    Value=orderValue + 10
    print('Oops! Value under $50, extra $10 will be charged for shipping')
    print(" Your order is billed for $ {0:f}".format(Value)
else:
    print('Enjoy your free shipping, your order is billed for $ {0:f}'.format(orderValue)
print('Happy ordering!')

