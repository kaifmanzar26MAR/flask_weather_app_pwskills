# from flask import Flask , render_template, request
from flask import Flask, request,render_template
import requests

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route("/weatherapp",methods=['POST',"GET"])
def get_weather():
    url="https://api.openweathermap.org/data/2.5/weather"
    city=request.form.get("city")
    id=request.form.get("appid")
    unit=request.form.get("units")
    param={
        'q':city,
        'appid':id,
        'units':unit
    }
    print(f"{city} {id}")
    response=requests.get(url,params=param)
    data=response.json()
    return f"data= {data}"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=3003)