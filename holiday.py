# Receives user inputs and assigns each to a variable, with the numeric inputs converted to integers
# While loops with if else and try except statements provide input validation
while True:
    city_flight = input("Please enter the city you are flying to. Your choices are Hanoi, Saigon and Da Nang: ")
    city_flight.lower()
    if city_flight == "hanoi" or city_flight == "saigon" or city_flight == "da nang":
        break
    else:
        print("You entered an invalid input")

while True:
    try:
        num_nights = int(input("Please enter the number of nights you will be staying at a hotel: "))
        break
    except ValueError:
        print("You entered an invalid input, please ensure that you enter an integer")

while True:
    try:
        rental_days = int(input("Please enter the number of days you will be renting a car: "))
        break
    except ValueError:
        print("You entered an invalid input, please ensure that you enter an integer")


# Defines a function that uses the num_nights user input and multiplies it by the nightly cost of a hotel, being 100 pounds
def hotel_cost(days):
    cost = days*100
    return cost

# Defines a function that uses if and elif statements to return a flight cost depending on the string the user inputted to the city_flight variable
def plane_cost(destination):
    if destination == "hanoi":
        cost = 350
    elif destination == "saigon":
        cost = 470
    elif destination == "da nang":
        cost = 300
    return cost

# Defines a function that multiplies the number of rental days inputted by the daily cost of renting a car, 50 pounds
def car_rental(days):
    cost = days*50
    return cost

# Defines a function that sums the costs of the previous functions
def holiday_cost(hotel, plane, car):
    cost = hotel + plane + car
    return cost

# Prints each of the costs determined by the various functions
print("The total cost of the hotel after staying for " + str(num_nights) + " nights is: " + str(hotel_cost(num_nights)) + " pounds.")
print("The cost of the flight to " + city_flight + " is: " + str(plane_cost(city_flight)) + " pounds.")
print("The total cost of renting the car for " + str(rental_days) + " days is: " + str(car_rental(rental_days)) + " pounds.")
print("The total cost of the holiday is: " + str(holiday_cost(hotel_cost(num_nights), plane_cost(city_flight), car_rental(rental_days))) + " pounds.")
