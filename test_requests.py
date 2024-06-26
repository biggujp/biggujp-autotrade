import requests
r = requests.post('https://10c2-58-8-212-139.ngrok-free.app/binance', 
                        json={
                                "action" : "TPSL SHORT",
                                "symbol" : "BTCUSDT",
                                "amount" : 0.04,
                        })

print(r.text)


