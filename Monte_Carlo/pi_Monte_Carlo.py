from __future__ import division
import numpy as np 
from bokeh.plotting import figure, show
from bokeh.plotting import *
import math
import random


# generate some random points
# equation --> x**2 + y**2 <= size

points_in = 0 # number of points inside the circle
points_out = 0 # number of points outside the circle
square_size = 1
sample = 1000
arc = np.linspace (0, np.pi/2, 100)

def generate (size):
	x = random.random() * size
	y = random.random() * size
	return (x,y)

def in_circle (point, size):
	return math.sqrt(point[0]**2 + point[1]**2)<= size

def pi(points_in, points_out): # calculate pi value
	return 4*(points_in / points_out)

t = figure (title ="Approximate value of pi", plot_width = 600, plot_height = 700)
for i in range (sample):
	point = generate (square_size)
	t.circle(point[0], point[1], color ="orange") 
	points_out +=1
	if in_circle(point, square_size):
		points_in +=1

print ("Approximate value of pi {}".format (pi(points_in, points_out)))

t.line(1*np.cos(arc), 1*np.sin(arc) , color = "black")
show (t)