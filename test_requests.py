import requests
r = requests.post('https://127.0.0.1:5000/binance', 
                        json={
                                "action" : "TPSL SHORT",
                                "symbol" : "BTCUSDT",
                                "amount" : 0.04,
                        })

print(r.text)