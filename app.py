import urllib.request
import json


from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/weather/')
@app.route('/weather/<name>')
def weather(name=None):
    f = urllib.request.urlopen('http://api.wunderground.com/api/7f38221bbed0e6fe/geolookup/conditions/q/VA/Winchester.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    location = parsed_json['location']['city']
    temp_f = parsed_json['current_observation']['temp_f']
    wind = parsed_json['current_observation']['wind_mph']
    return "Current temperature in %s is: %s and the wind speed is currently %s miles per hour." % (location, temp_f, wind)
    f.close()


if __name__ == '__main__':
    app.run()