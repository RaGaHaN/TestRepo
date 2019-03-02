
#Total number of cars
cars = 100
#Space in each car that can accomodate the passenger
space_in_a_car = 4.0
#Total number of drivers that particular day
drivers = 30
#Total number of passengers need to travel
passengers = 90
#Cars that are idle due to non-availability of drivers
cars_not_driven = cars - drivers
#Total cars driven by the drivers, one for each driver
cars_driven = drivers
#How many people the cars available can accomodate
carpool_capacity = cars_driven * space_in_a_car
#Minimum number of passengers that can get in to a car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars availabel")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars available")
print("We can transport", carpool_capacity, "people today")
print()
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")
