# Use string concatenation and the len function to find the length of a certain movie star's actual full name. 
# Store that length in the name_length variable. Don't forget that there are spaces in between the different parts of a name!

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

# Solution: 
name_length = len(given_name) + len(middle_names) + len(family_name)

# Now we check to make sure that the name fits within the driving license character limit, which is 25

# Solution :
if name_length <= 25:
    print("within character limit")
else:
    print("to reduce characters")
