import requests
r = requests.post('http://127.0.0.1:5000/webhook/binance_future', 
                        json={
                                "ACTION" : "TPSL SHORT",
                                "SYMBOL" : "BTCUSDT",
                                "AMOUNT" : 0.04,
                        })

print(r.text)