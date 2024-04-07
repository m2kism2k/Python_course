order_list=[2, 4, 5, 6]
price=4.55
amount_list = []
for i in oreder_list:
  amount =0
  amount = i * price
  amount_format = "{:.2f}".format(amount)
  amount_list.append(float(amount_format))

print("Amount List : "+str(amount_list))
