"""
Define a class named Point that has the following specification:

Attributes

(1) x: int, x-coordinate of the point in 2D space.
(2) y: int, y-coordinate of the point in 2D space.

Methods

self is the first argument of all methods. We will only mention the additional arguments, if any.

(1) __init__: constructor with two arguments — x and y; assign these two values to the corresponding attributes within the constructor
(2) distance: return the distance of the point from the origin as a float value
(3) is_origin: return True if the point coincides with the origin, and False otherwise
(4) on_xaxis: return True if the point is on the x-axis, and False otherwise
(5) on_yaxis: return True if the point is on the y-axis and False otherwise
(6) quadrant: return the quadrant that this point belongs to; assume that this method will only be called if the point is not on either of the axes; possible return values are ['first', 'second', 'third', 'fourth'].
(7) slope: return the slope of the line joining the origin and this point as a float value; assume that this method will only be called if the point is not on the y-axis
"""
import math
class Point:
    x:int
    y:int
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self):
        return math.sqrt((self.x**2) + (self.y**2))
    
    def is_origin(self):
        if self.x == 0 and self.y == 0:
            return True
        else:
            return False
    
    def on_xaxis(self):
        if self.y == 0:
            return True
        else:
            return False
    
    def on_yaxis(self):
        if self.x == 0:
            return True
        else: 
            return False
    
    def quadrant(self):
        if(self.x > 0 and self.y > 0):
            return "first"
        if(self.x < 0 and self.y > 0):
            return "second"
        if(self.x < 0 and self.y < 0):
            return "third"
        if(self.x > 0 and self.y < 0):
            return "fourth"
    
    def slope(self):
        return self.y/self.x
    
"""
Consider an intelligent traffic signal. The signal has two states: red and green. The vehicle density in front of the signal is denoted by the variable 
v
v. If the vehicle density crosses a threshold 
T
T in either direction, the state of the signal changes. The dynamics of this change is represented in the image given below:

image-20211103123731715

For example, if the signal is currently red, and the vehicle density becomes greater than or equal to the threshold, it is time to turn the signal green. This is denoted by the arrow from red to green at the bottom of the image. Assume that the signal senses the vehicle density every 30 seconds and updates its state appropriately.

Write a class named Signal with the following specification:

Attributes

(1) state: string, either "red" or "green"; represents the current state of the signal
(2) v: int, represents the vehicle density at the current instant
(3) T: int, threshold for the vehicle density

Methods

self is the first argument of all methods. We will only mention additional arguments, if any.
(1) __init__: constructor; accepts the threshold T as argument; initially the signal is red and the vehicle density is 0.
(2) sense: accept the vehicle density as argument and update the corresponding attribute; assume that this information comes from a sensor.
(3) update: update the state of the signal-attribute depending on the current values of the attributes.
"""

class Signal:
    def __init__(self, T):
        self.T:int = T
        self.state: str = "red"
        self.v:int = 0
        
    def sense(self, v):
        self.v = v
        self.update()
    
    def update(self):
        if self.state == "red":
            if self.v >= self.T:
                self.state = "green"

        if self.state == "green":
            if self.v < self.T:
                self.state = "red"


