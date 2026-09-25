# Some useful functions for various tasks
# Helpful way of testing these is to break the code into cells using # %%

#Print functions

#SEP seperator

team = "Finance"
spend = 1000
print("Team:", team, "Spend:", spend, sep=" | ") 

#End - do not incude new line in the print statement
#Example, both will appear on the same line
print("Hello", end=" ")
print("World!")

#Help - get the doc string for a function
help(print)

def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.
    a: value 1
    b: value 2
    
    returns: int
    """
    return a + b

print(add_numbers(5, 10))  # Output: 15
help(add_numbers)  # Displays the docstring for the add_numbers function


#Rng range - creates a list of numnbers
#Returns an iterable object. Use list() to convert it to a list

rng = range(10)
print(list(rng)) #output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Starts at 2, ends at 20, increments by 2
rng = range(2,20,2)
print(list(rng)) #output: [2, 4, 6, 8, 10, 12, 14, 16, 18]

#Map. Applies a function to each item in an iterable
strings = ["one", "two", "three", "four", "five"]
lengths = map(len, strings)
print(list(lengths)) #output: [3, 3, 5, 4, 4]

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers) #output: [1, 4, 9, 16, 25]
 
#Filter. Filters items in an iterable based on a condition
def is_even(n):
    return n % 2 == 0   

#Uses the is_even function in the filter
filtered_numbers = filter(is_even, numbers)
print(list(filtered_numbers)) #output: [2, 4]

#Uses a lambda function in the filter. Moved list to the function call, not print statement
filtered_numbers = list(filter(lambda x: x > 2, numbers))
print(filtered_numbers) #output: [3, 4, 5]

#sum with start. Sums the items in an iterable, starting from a specified value
total = sum(numbers, start=3)
print(total) #output: 18 (1+2+3+4+5 + 3)

#sorted. Sorts the items in an iterable and returns a new sorted list
unsorted_numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(unsorted_numbers)
print(sorted_numbers) #output: [1, 2, 5, 5, 6, 9]

sorted_numbers = sorted(unsorted_numbers, reverse=True)
print(sorted_numbers) #output: [9, 6, 5, 5,