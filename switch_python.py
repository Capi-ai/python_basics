# Function to convert string into number
# Python has no switch option
#     so dictionary is used instead

def string_to_integer(argument):
    switcher = {
               "zero": 0,
               "one" : 1,      
               "two" : 2      
	       }
    # get() method used to return
    # the value of the dictionary where
    # "argument" is the key
    # If no argument found, then "nothing"
    # is return
    return switcher.get(argument, "nothing")

# Driver program
if __name__ == "__main__":
    num_str_1 = "two"
    num_str_2 = "five"
    print(string_to_integer(num_str_1))
    print(string_to_integer(num_str_2))



