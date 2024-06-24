import requests
r = requests.post('https://biggujp-webhook-746a56632c2c.herokuapp.com/webhook/binance_future', 
                        json={
                                "action" : "TPSL SHORT",
                                "symbol" : "BTCUSDT",
                                "AMOUNT" : 0.04,
                        })

print(r.text)