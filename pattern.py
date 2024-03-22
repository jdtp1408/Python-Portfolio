# for loop iterates through the necessary number of lines and print the pattern
for i in range(1,11):
    print_pattern = "*" * i

# if statement to reverse order
    if i >= 6:
        print_pattern = (10 - i) * "*"
    
    print(print_pattern)
    