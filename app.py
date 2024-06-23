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
        signal = request.data.decode("utf-8")
        signal_as_dictionary = json.loads(signal)
        print(signal_as_dictionary)
        
        trade_side = signal_as_dictionary["ACTION"]
        trade_symbol = signal_as_dictionary["SYMBOL"]
        trade_amount = signal_as_dictionary["AMOUNT"]
        
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

    
