#Question 3: Power of Two 
number = int(input("Enter a number: "))

if (number != 0) and (number & (number - 1)) == 0:
    print(f"{number} True")
else:
    print(f"{number} False")
