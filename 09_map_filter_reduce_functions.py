import math
import numpy

def area(r):
    """Area of a circle with radius 'r'. """
    return math.pi * (r ** 2)


radii = [2, 5, 7.1, 0.3, 10]

# Method 1: Direct method
areas = []
for i in radii:
    a = area(i)
    areas.append(a)

print "Method 1:", areas, "\n"


# Method 2: Use 'map' function
print "Method 2 (using 'map' function):", map(area, radii), "\n"  # output will be an map object


# Convert Celsius to Fahrenheit F = 9/5*C + 32
temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("Tokio", 27), ("New York", 28),
         ("London", 22)]

c_to_f = lambda data: (data[0], (9 / 5) * data[1] + 32)

print "Converting Celsius to Fahrenheit:", map(c_to_f, temps), "\n"


# Average data
data = [2.3, 1.2, 3.1, 5.2, 6, 4.3]
avg = numpy.std(data)

print "Average is:", avg

