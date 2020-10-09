#!/usr/bin/env python

__author__ = 'Leann James with help from Joseph Hafed (on part A)'

import requests
from datetime import datetime


def astronaut_names():
    response = requests.get("http://api.open-notify.org/astros.json")
    astronaut_info = response.json()
    list_of_info = astronaut_info.get('people')
    print(f'number of people on ISS: {astronaut_info.get("number")}')
    for i in list_of_info:
        print(f'{i.get("name")} is on {i.get("craft")}')


def location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    location_info = response.json()
    position = location_info.get('iss_position')
    latitude = position.get('latitude')
    longitude = position.get('longitude')
    timestamp = location_info.get('timestamp')
    time = datetime.fromtimestamp(timestamp)
    print(f'The ISS is currently at: {latitude}, {longitude}')
    print(time)


def main():
    astronaut_names()
    location()


if __name__ == '__main__':
    main()
