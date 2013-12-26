name = 'David C. Kuo'
age = 27
height_in = 71 #inches
weight_lb = 168 #pounds
eyes = 'Brown' 
teeth = 'White'
hair = 'Brown'
height_cm = height_in * 2.54
weight_kg = weight_lb * 0.453592

print "Let's talk about %s." % name
print "He's %d inches tall in inches." % height_in
print "He's %d inches tall in centimeters" % height_cm
print "He's %d pounds heavy in lb." % weight_lb
print "He's %d pounds heavy in kg." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (
	age, height_in, weight_lb, age + height_in + weight_lb)
