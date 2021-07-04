!pip install coinbase
!pip install smtplib
from coinbase.wallet.client import Client

from time import sleep
# Python code to illustrate Sending mail from
# your Gmail account
import smtplib


#from data import percentage_change, api_key, api_secret
api_key = ""  # emailme :nikhilmatta10@gmail.com
api_secret = "" #emailme : nikhilmatta10@gmail.com
def percentage_change(x,y):
  return ((eval(x) - eval(y))/eval(x))*100

#https://developers.coinbase.com/docs/wallet/guides/buy-sell


#Setting up coinbase client

client = Client(api_key, api_secret)

#payment_method = client.get_payment_methods()[0] //USED TO GRAB PAYMENT ID TO ACTUALLY MAKE THE PURCHASE


#Take user input

user_limit_order = float(input("Enter a price for your Bitcoin limit order (USD): "))

user_amount_spent = float(input("Enter how much you want to spend (USD): "))


#Creating the loop

currency_code = 'USD'

payment_methods = client.get_payment_methods()
print(payment_methods)
start_price = client.get_spot_price(currency=currency_code)


#help(client.get_primary_account)
#help(client.get_payment_methods())
#account = client.get_primary_account()

#payment_method = client.get_payment_methods()[0]

while(True):


    #Reset currents and find percentage change
    print("old_rate ",user_limit_order)
    buy_price = client.get_buy_price(currency=currency_code)
    buy_price = eval(buy_price.amount)
    if buy_price+50.0 > user_limit_order-50.0 :
      user_limit_order = buy_price - 50
      message = "WE ARE GOING UP" + str(user_limit_order)
      print("WE ARE GOING UP ",user_limit_order)
    elif user_limit_order-10 > buy_price:
      message = "SELL"
      print("SELL")

    # email
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("youremail", "pswrd")



    s.sendmail("youemail", "recieveremail",message )
    s.quit()





    #percentage_gainloss = percentage_change(start_price.amount, buy_price.amount)


    #print bitcoin curent price, and percentage chage

    #print('Bitcoin is ' + str(buy_price.amount) + '\nPercent change in last 60 seconds: ' + format(percentage_gainloss, ".3f") + '%')


    #Within Purchase Threshold

    #if(float(buy_price.amount) >= user_limit_order):


 #      buy = client.buy(amount=str(user_amount_spent / float(buy_price.amount), currency=currency_code, payment_method=payment_method.id))


        #print("Bought $" + str(user_amount_spent) + " or " + str(user_amount_spent / float(buy_price.amount)) + " bitcoin at " + buy_price.amount)


    sleep(60)


    #Update start_price

    start_price = buy_price


