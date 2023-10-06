import time
import kml2geojson
import pandas
from streamer import Streamer


def start_loop():
    i = 0
    global randomizer
    while i < len(bus_waypoints):
        streamer.push('prod/chn/LM29/sen', {
            'dID': 'LM29',
            'sog': 4,
            'lat': bus_waypoints[i][1],
            'long': bus_waypoints[i][0]
        })
        i += 1
        # if randomizer:
        #     i -= 1
        #     randomizer = False
        #     print('INFO: Going backwards')
        # else:
        #     i += 1
        #     if i % 30 == 0:
        #         randomizer = True
        #     print('INFO: Going forwards')
        time.sleep(5)


randomizer = False
bus_waypoints = [[row['value.lon'], row['value.lat']] for i, row in pandas.read_csv('LM30A.csv').iterrows()]
# route = kml2geojson.convert('route.kml')[0]['features'][0]['geometry']['coordinates']
streamer = Streamer(host='broker', port=1883)
streamer.start()
start_loop()
