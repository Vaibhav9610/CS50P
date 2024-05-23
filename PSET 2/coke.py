print("Amount Due: 50")
amount_due=50


while amount_due>=0:
   insert=int(input("Insert Amount(5,15,25): "))
   amount_due=amount_due-insert
   if amount_due>=0:
       print("Amount Due: "+str(amount_due))
   else:
       print("change owed: "+str(-amount_due))