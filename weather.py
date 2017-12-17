import urllib.request
import json

class Weather:
    """docstring for ClassName"""


    def get_location(self):
        #function to fetch and parse location/weatherdata from wunderground API
        get_location = input("What is the url of location?: ")
        f = urllib.request.urlopen(get_location)
        json_string = f.read()
        self.parsed_json = json.loads(json_string)



    def weather_data_params(self):
        #take parsed json and ask for user input. Turn user input into dictionary? keys. Ask for two values.
        get_info = input("what data do you want? (enter as INPUT,INPUT): ")
        first, second = get_info.split(',')
        location = self.parsed_json[first][second]
        get_info2 = input("what data do you want? (enter as INPUT,INPUT or IDK): ")
        if get_info2 == 'IDK':
            x = input("would you like to see what options you have? Y or N: ")
            if x == "Y":
                self.display()
            if x == "N":
                print("Okay")



        third, fourth = get_info2.split(',')
        temp_f = self.parsed_json[third][fourth]
        wind = self.parsed_json['current_observation']['wind_mph']
        print("Current temperature in %s is: %s and the wind speed is currently %s miles per hour." % (location, temp_f, wind))

    def display(self):
        print(json.dumps(self.parsed_json))




w = Weather()
w.get_location()
w.weather_data_params()







