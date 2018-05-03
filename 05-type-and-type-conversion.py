# Exercise 1
# Use this program to experiment with types of objects.
# Don't forget to use print to see the results of your code.

wholeNumber = 10
decimalNumber = 10.05
word = "name"

# Solutions:
print(type(wholeNumber))
print(type(decimalNumber))
print(type(word))

# Exercise 2
# Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

# Solutions:

# cast the String to integer and store all total value to weekly_sales variable
weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)

# print the value by casting it back to String
print("This week's total sales: " + str(weekly_sales))

