import requests
import webbrowser
import time
import turtle

# Opening a screen for turtle
screen = turtle.Screen()
# Keeps the screen open
turtle.mainloop()

"""
astronaut_data = 'http://api.open-notify.org/astros.json'

result = requests.get(astronaut_data).json()

print(result)

print('People in space {}'.format(result['number']))

# Iterating in peoples list.
for person in result['people']:
    print(person['name'] + ' in ' +  person['craft'])


iss_status = 'http://api.open-notify.org/iss-now.json'

while True:
    result = requests.get(iss_status).json()
    timestamp = result['timestamp']
    lat = result['iss_position']['latitude']
    long = result['iss_position']['longitude']
    print('LAT : {}, LONG : {}, TIMESTAMP : {}'.format(lat, long, str(timestamp)))
    time.sleep(.1)



#google_maps = 'http://maps.google.com/?q={},{}'.format(lat,long)
#webbrowser.open_new_tab(google_maps)
"""
