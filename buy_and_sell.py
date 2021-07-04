import cbpro
BUY = "buy"
SELL = "sell"

class TradingSystems:
  def __init__(self,cb_pro_client):
    self.client = cb_pro_client

  def trade(self,action,limitPrice,quantity):
    if action == BUY:
      response = self.client.buy(price = limitPrice,size=self.round(quantity),order_type="limit",product_id = "BTC-USD",overdraft_enabled=False)
    elif action == SELL:
      response = self.client.sell(price = limitPrice,size=quantity,order_type="limit",product_id = "BTC-USD",overdraft_enabled=False)

    print(response)
      
    

  #def viewAccounts(self,accountCurrency):
    #accounts = self.client.get_accounts()
    #account = list(filter(lambda x:x["currency"] == accountCurrency,accounts))[0]
    #return account

  def viewOrder(self,order_id):
    return self.client.get_order(order_id)

  def round(self,val):
    newval = int(val * 10000000/10000000)
    return newval


  def gettingCurrentPriceOfBitcoin(self):
    tick = self.client.get_product_ticker(product_id="BTC-USD")
    return tick["bid"]

if __name__ == "__main__":
  auth_client = cbpro.AuthenticatedClient(cbpro_pubkey,
                                          cbpro_secret,
                                          cbpro_passphrase,
                                          api_url="https://api-public.sandbox.pro.coinbase.com")
  
  TradingSystems = TradingSystems(auth_client)
  currentPrice = TradingSystems.gettingCurrentPriceOfBitcoin()
  #usdBalance = TradingSystems.viewAccounts("USD")["balance"]
  usdBalance=1000
  TradingSystems.trade(BUY,float(currentPrice),float(usdBalance)/float(currentPrice))
