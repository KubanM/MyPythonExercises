# Anonymous Function = Lambda Expression

# Write function to compute 3x+1
def f(x):
    return 3*x + 1

print f(2), "\n"

g = lambda x: 3*x+1
print "Lambda:",  g(2), "\n"


#Combaine first name and last name into a single fullname
fullname = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

print fullname("  leonard", "EULER"), "\n"


#Create a Lambda expression which will be extract a last names and use that as sorting value
scifi_authors = ["Isaac Azimov", "Ray Bradbry", "Robert Heinlein", "Arthus C. Clarke", "Frank Herbert", "Orson Scott Cart", "Douglas Adams", "H. G. Wells", "Leigh Bracket"]

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())

print scifi_authors, "\n"


#Quadratic Functions f(x) = ax^2 + bx + c
def build_quadratic_function(a, b, c):
    """ Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

print  build_quadratic_function(3, 0, 1)(2), "\n"

