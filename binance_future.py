import ccxt
from config import *

#Get balance from wallet
binance_future = ccxt.binance({
    'apiKey' : BINANCE_FUTURE_API_KEY,
    'secret' : BINANCE_FUTURE_API_SECRET,
    'options' : {
        'defaultType' : 'future',
        'adjustForTimeDifference':True
    }
})
binance_future.set_sandbox_mode(BINANCE_FUTURE_TESTING)


time = binance_future.fetch_time()
print(binance_future.iso8601(time))

#future_balnance = binance_future.fetch_balance()
#my_USDT = future_balnance["USDT"]["free"]
#my_position_size = float(my_USDT) * 0.01
#print("My Balnance : {}".format(my_USDT))
#print("My Position size : {}".format(my_position_size))




#Place order
#margin Risk per trade 1% => my_position_size
#3% stoploss fix (previous candles low)
#position size margin x leverage
#leverage => 20x
#cross margin
# my_symbol="BTCUSDT"
#my_leverage = 20

# get_current_btc_price = binance_future.fetch_last_prices([my_symbol])
# current_btc_price = float(list(get_current_btc_price.values())[0]["price"])
#binance_future.set_leverage(my_leverage,my_symbol)
# calculation_amount = my_position_size * my_leverage / current_btc_price
# print(calculation_amount)

# binance_future.create_order(
#     symbol=my_symbol,
#     type="market",
#     side="buy",
#     amount=calculation_amount
# )

def order_long(symbols,amount):
    my_leverage = 20
    binance_future.set_leverage(my_leverage,symbols)
    binance_future.create_order(
        symbol=symbols,
        type="market",
        side="buy",
        amount=float(amount),
        )
    
def order_tpsl_long(symbols,amount):
    my_leverage = 20
    binance_future.set_leverage(my_leverage,symbols)
    binance_future.create_order(
        symbol=symbols,
        type="market",
        side="sell",
        amount=float(amount),
        )
        
def order_short(symbols,amount):
    my_leverage = 20
    binance_future.set_leverage(my_leverage,symbols)
    binance_future.create_order(
        symbol=symbols,
        type="market",
        side="sell",
        amount=float(amount),
        )
    
def order_tpsl_short(symbols,amount):
    my_leverage = 20
    binance_future.set_leverage(my_leverage,symbols)
    binance_future.create_order(
        symbol=symbols,
        type="market",
        side="buy",
        amount=float(amount),
        )

