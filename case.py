from urllib import request
import flask
import json, time
import requests, json

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    name_surname = {'name': 'Tarik.Tunahan', 'surname': 'Akan'}
    home_page = json.dumps(name_surname)
    return home_page

@app.route('/temperature&city=<city>', methods=['GET'])
def temperature_page(city):
    apikey = "9876fd2d4b8a4a6ba198bde135f43c98"     
    url = f'https://api.weatherbit.io/v2.0/current?&city={city}&key={apikey}&include=minutely'
    response = requests.get(url)
    data = response.json()['data'][0]
    temp = data['temp']
    print(f'Degrees: {temp}')

    temperature_city = {'temperature': temp}
    temperature_page = json.dumps(temperature_city)
    return temperature_page

   
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
