# Scalene triangle: All sides have different lengths.
# Isosceles triangle: Two sides have the same lengths
# Equilateral triangle: All sides are equal,

a = int(raw_input("The length of size a = "))
b = int(raw_input("The length of size b = "))
c = int(raw_input("The length of size c = "))

if a != b and b != c and c != a:
    print "This is a Scalence triangle"
elif a == b and b == c:
    print "This is an Equilateral triangle"
else:
    print "This is an Isosceles triangle"     
