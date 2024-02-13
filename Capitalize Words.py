#Question 4: Capitalize Words 
input_string = input("Enter a string: ")

words_list = input_string.split()

capitalized_words = [word.capitalize() for word in words_list]

result_string = " ".join(capitalized_words)

print("Result string: ", result_string)
