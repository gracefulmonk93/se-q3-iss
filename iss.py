#!/usr/bin/env python

__author__ = '''Leann James with help from Joseph Hafed (on part A)
                and Jordan Haagenson (on part C and D)'''

import requests
from datetime import datetime
import turtle
import time


def astronaut_names():
    response = requests.get("http://api.open-notify.org/astros.json")
    astronaut_info = response.json()
    list_of_info = astronaut_info.get('people')
    print(f'number of people on ISS: {astronaut_info.get("number")}')
    for i in list_of_info:
        print(f'{i.get("name")} is on {i.get("craft")}')


def location(Indianapolis=False):
    if not Indianapolis:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        location_info = response.json()
        position = location_info.get('iss_position')
        latitude = position.get('latitude')
        longitude = position.get('longitude')
        timestamp = location_info.get('timestamp')
        tme = datetime.fromtimestamp(timestamp)
        print(f'The ISS is currently at: {latitude}, {longitude}')
        print(tme)
        return location_info
    if Indianapolis:
        response = (requests.get(
                    "http://api.open-notify.org/iss-pass.json" +
                    "?lat=39.76&lon=-86.15"))
        response = response.json()
        tme = response['response'][0]['risetime']
        timestamp = time.ctime(int(tme))
        return timestamp


def setup(bg):
    screen = turtle.Screen()
    screen.setup(width=720, height=360, startx=0, starty=0)
    screen.setworldcoordinates(-180, -90, 180, 90)
    turtle.mode('world')
    screen.bgpic(bg)
    return screen


def mapped_location(longitude, latitude, Indianapolis=False):
    if not Indianapolis:
        icon = 'iss.gif'
        turtle.register_shape(icon)
        pen = turtle.Turtle(shape=icon)
        pen.penup()
        pen.setpos(float(longitude), float(latitude))
        return pen
    if Indianapolis:
        pen = turtle.Turtle(visible=False)
        pen.penup()
        pen.color('yellow')
        pen.setpos(float(longitude), float(latitude))
        pen.dot(10, 'yellow')
        return pen


def Indianapolis(timestamp=None):
    pen = mapped_location(-86.1581, 39.7684, True)
    if timestamp is not None:
        pen.write(timestamp, align='right', font=('Comic Sans', 10, 'bold'))


def main():
    astronaut_names()
    loc = location()
    setup('map.gif')
    mapped_location(-86.1581, 39.7684, True)
    t = location(True)
    mapped_location(loc['iss_position']['longitude'],
                    loc['iss_position']['latitude'])
    Indianapolis(t)
    turtle.Screen().exitonclick()


if __name__ == '__main__':
    main()
