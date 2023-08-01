import time
from streamer import Streamer


def start_loop():
    streamer.push('dev/cam1', {
        'Id': 'xxx',
        'Status': 'xxx',
        'Timestamp': 'xxx',
        'Price': 'xxx',
        'Price/ml ': 'xxx',
        'Manufacturing Date': 'xxx',
        'Expiry Date': 'xxx',
        'Batch No.': 'xxx',
        'Other Code': 'xxx',
        'Batch Time': 'xxx'
    })
    time.sleep(1)
    start_loop()


streamer = Streamer(host='broker', port=1883)
streamer.start()
start_loop()
