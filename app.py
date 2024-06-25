from binance_future import order_long,order_short,order_tpsl_long,order_tpsl_short
from flask import Flask,request,render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/webhook/binance_future",methods = ["GET","POST"])
def webhook_binance_future():        
    if request.method == "GET":
        return "<p> This is route for POST METHOD FOR binance_future !</p>"
    elif request.method == "POST":
        # json == dictionary python
        #signal = request.data.decode("utf-8")
        signal = json.loads(signal)

        # format data string --> json
        signal = signal.split("\n")[0] # {'action':'TPSL LONG','exchange':'BINANCE','symbol':'BTCUSDT'}
        signal = signal.replace("'",'"')
        trade_side = signal["action"]
        trade_symbol = signal["symbol"]
        trade_amount = 0.044
        
        if "LONG" in trade_side:
                order_long(trade_symbol,trade_amount)
                # เรียกฟังก์ชั่นในการเปิดสัญญาLONG ส่งไปที่ Exchange , Broker

                pass
        
        elif "SHORT" in trade_side:
                order_short(trade_symbol,trade_amount)
                # เรียกฟังก์ชั่นในการเปิดสัญญาSHORT ส่งไปที่ Exchange , Broker
                pass
        
        elif "TPSL LONG" in trade_side:
                order_tpsl_long(trade_symbol,trade_amount)
                # เรียกฟังก์ชั่นในการปิดสัญญาLONG ส่งไปที่ Exchange , Broker
                pass
        
        elif "TPSL SHORT" in trade_side:
                order_tpsl_short(trade_symbol,trade_amount)
                # เรียกฟังก์ชั่นในการปิดสัญญาSHORT ส่งไปที่ Exchange , Broker
                pass
        
        return "200"
    
if __name__ == "__main__":
    app.run(debug=True)

    
