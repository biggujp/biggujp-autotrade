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

@app.route('/autotrade')
def autotrade():
    return render_template("autotrade.html")

@app.route("/binance",methods = ["GET","POST"])
def webhook_binance_future():        
    if request.method == "GET":
        return "<p> This is route for POST METHOD FOR binance_future !</p>"
    elif request.method == "POST":
        print("ได้รับคำสั่งซื้อขายจาก tradingview")
        # json == dictionary python
        #signal = request.data.decode("utf-8")
        signal_as_dic = json.loads(request.data) 
        print(signal_as_dic)
        signal_as_dic = signal_as_dic['tvs']
        signal_as_dic = signal_as_dic.split("\n")[0]
        signal_as_dic = signal_as_dic.replace("'",'"')
        signal = json.loads(signal_as_dic)
        print(signal)

        exchange = signal["exchange"]
        action = signal["action"]
        symbol = signal["symbol"]
        amount = float(0.044)
        
        if "LONG" in action:
                order_long(symbol,amount)
                # เรียกฟังก์ชั่นในการเปิดสัญญาLONG ส่งไปที่ Exchange , Broker

                pass
        
        elif "SHORT" in action:
                order_short(symbol,amount)
                # เรียกฟังก์ชั่นในการเปิดสัญญาSHORT ส่งไปที่ Exchange , Broker
                pass
        
        elif "TPSL LONG" in action:
                order_tpsl_long(symbol,amount)
                # เรียกฟังก์ชั่นในการปิดสัญญาLONG ส่งไปที่ Exchange , Broker
                pass
        
        elif "TPSL SHORT" in action:
                order_tpsl_short(symbol,amount)
                # เรียกฟังก์ชั่นในการปิดสัญญาSHORT ส่งไปที่ Exchange , Broker
                pass
        
        return "200"
    
if __name__ == "__main__":
    app.run(debug=True)

    
