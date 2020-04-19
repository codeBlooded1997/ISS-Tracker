import requests
import webbrowser
import time
import turtle


astronaut_data = 'http://api.open-notify.org/astros.json'

result = requests.get(astronaut_data).json()

print(result)

print('People in space {}'.format(result['number']))

# Iterating in peoples list.
for person in result['people']:
    print(person['name'] + ' in ' +  person['craft'])


iss_status = 'http://api.open-notify.org/iss-now.json'

while True:
    # Getting the iss json data using NASA REST API
    result = requests.get(iss_status).json()
    # Extracting data : TIMESTAMP, LAT, LONG
    timestamp = result['timestamp']
    lat = result['iss_position']['latitude']
    long = result['iss_position']['longitude']
    # Showing extracted data in the console
    print('LAT : {}, LONG : {}, TIMESTAMP : {}'.format(lat, long, str(timestamp)))
    # Opening a screen for turtle.
    screen = turtle.Screen()
    # Specifiying dimentions.
    screen.setup(720,360)
    # Defining cordinantes so we can pass in lat and long
    screen.setworldcoordinates(-180, -90, 180, 90)
    # Setting backgroung image
    screen.bgpic('Nasa_World_Map.gif')
    # Registering our ISS shape
    screen.register_shape('ISS.gif')
    # Creating turtle
    iss = turtle.Turtle(visible=False)
    # Setting registered shape as cursor!
    iss.shape('ISS.gif')
    # Hiding the line behind our shape
    iss.penup()
    # Moving Turtle
    iss.goto(float(long),float(lat))
    # Showing shape again
    iss.showturtle()
    # Keeps the screen open.
    #turtle.mainloop()
    # updates the app every .1 second
    time.sleep(.1)


#google_maps = 'http://maps.google.com/?q={},{}'.format(lat,long)
#webbrowser.open_new_tab(google_maps)
