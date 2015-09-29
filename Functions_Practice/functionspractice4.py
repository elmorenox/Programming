"""Write a program to calculate the area of four different geometric shapes: triangles, squares, rectangles, and circles.
You must use functions. Your program should present a menu for the user to choose which shape to calculate, 
then ask them for the appropriate values (length, width, radius, etc.).
Then it should pass those values to the appropriate function and display the resulting area."""

def areaTriangle(base,height):
	area = (base * height) / 2
	return area

def areaRectangle(base,height): 
	area = (base * height)
	return area

def areaSquare(side): 
	area = side**2
	return area

def areaCircle(radius): 
	area = (3.14) * (radius**2)
	return area

print "Find the area of a shape."
print "1 for Trinagle"
print "2 for Rectangle"
print "3 for Square"
print "4 for Circle"

shapeSelect = raw_input("Select a shape: ")

if shapeSelect == "1":
	base = int(raw_input("What is the base?: "))
	height = int(raw_input("What is the height?: "))
	print "The area is %s units" %areaTriangle(base,height)

elif shapeSelect == "2": 
	base = int(raw_input("What is the base?: "))
	height = int(raw_input("What is the height?: "))
	print "The area is %s units" %areaRectangle(base,height)

elif shapeSelect == "3": 
	side = int(raw_input("What is the lenght of a side?: "))
	print "The area is %s units" %areaSquare(side)

elif shapeSelect == "4": 
	radius = float(raw_input("What is the radius?: "))
	print "The area is %s units" %areaCircle(radius)

	


