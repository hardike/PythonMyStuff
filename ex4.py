# We have a total of 100 cars
cars = 100

#Each car can hold 4 people
space_in_a_car = 4.0

#We have 30 drivers
drivers = 30

# We have 90 passengers
passengers = 90

# Cars without drivers
cars_not_driven = cars - drivers

# Cars with drivers
cars_driven = drivers

# Total capacity using CarPools
carpool_capacity = cars_driven * space_in_a_car

# Average number of people to be held per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


