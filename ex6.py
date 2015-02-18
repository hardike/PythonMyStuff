x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)    #place 1

print x
print y

print "I said: %r." %x		#place2
print "I also said: '%s'." %y      ##place3

hilarious = False
joke_evaluation = "Isnt that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with the right side."

print w + e  #place4
