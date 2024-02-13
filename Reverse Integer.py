#Question 5: Reverse Integer 
number = int(input("Please enter an integer: "))

reversed_number = 0

while number != 0:
    
    digit = number % 10

    reversed_number = reversed_number * 10 + digit

    number = number // 10
    
print("Reversed integer: ", reversed_number)
