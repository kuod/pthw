#joke statement
x = "There are %d types of people." % 10
#two types
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
#print strings
print x
print y
#repeat x except with quotes
print "I said: %r." % x
#repeat y except with quotes
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#joke_evaluation needs %r, give hilarious
print joke_evaluation % hilarious

#Two strings
w = "This is the left side of..."
e = "a string with a right side."

print w + e
