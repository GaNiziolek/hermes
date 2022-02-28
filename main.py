import gpsd
import requests
import os

API_URL = os.getenv('HERMES_LOGGER_URL')

def main():
    gpsd.connect()

    pos = gpsd.get_current()

    if pos.mode >= 2:

        time = pos.get_time()

        data = {
            'timestamp': f'{time.year}-{time.month}-{time.day} {time.hour}:{time.minute}:{time.second}',
            'longitude': pos.lon,
            'latitude': pos.lat
        }

        response = requests.post(API_URL, json=data)
        print(response.json())
        
if __name__ == "__main__":
    try:
        main()
    except:
        pass