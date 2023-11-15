from flask import Flask

app = Flask(__name__) # app değişkenizimizin Flask olduğunu belirttik.

@app.route("/") # Endpoint imizi tanımladık.
def hello(): # Bir fonksiyon oluşturduk.
    return "Hello World" # Sitemizde görmek istediğimiz şeyi return ettik.