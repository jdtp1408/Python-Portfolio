# Variables values defined to offset the -1 exit input
user_num = 0
user_sum = 1
count = -1

# While loop operates while user input is not -1, counts number of inputs and sums each input
while user_num != -1:
    user_num = int(input("Enter numbers to be averaged and enter -1 to calculate the average: "))
    user_sum += user_num
    count += 1

# Calculates and prints average if count is greater than 0
if count > 0:
    avg = user_sum/count
    print("The average of the inputted numbers is: " + str(avg))
else:
    print("There were no numbers to average")