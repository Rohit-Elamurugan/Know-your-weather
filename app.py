from flask import Flask, render_template
import requests, json
api_key = "7e1a3c93792ff149f4bfe2a5a2f66562"
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/place/<place>')
def weather(place):
    complete_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + api_key + "&q=" + place
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        tempK = round(x["main"]["temp"],)
        tempC = round(tempK - 273.15,2)
        tempF = round(tempC * 9/5 + 32,2)
        pressure = x["main"]["pressure"]
        humidiy = x["main"]["humidity"]
        description = x["weather"][0]["description"]
        return render_template('page.html',place=place,info="Temperature = " + str(tempC) + " °C"
                                                            "<br/>Temperature = " + str(tempF) + " °F"
                                                            "<br/>Temperature = " + str(tempK) + " K"
                                                            "<br/>Atmospheric pressure = " + str(pressure) + " hPa"
                                                            "<br/>Humidity = " + str(humidiy) + " %"
                                                            "<br/>Description = " + str(description))
    else:
        return render_template('page.html',info='No details about that city :(')
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
