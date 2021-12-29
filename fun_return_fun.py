# USAGE
# python fun_return_fun.py --operation add|subs|times|divide --num1 int --num2 int

#This script shows how
# functions can return another function
#Depending on the argument on main, will return one
# function or another

import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--operation", "-op", required=True,
               help="add, subs, times, divide")
ap.add_argument("--num1", "-n1", required=True,
             help="Enter first number involved in operation")
ap.add_argument("--num2", "-n2", required=True,
             help="Enter second number involved in operation")
args = vars(ap.parse_args())


def create_action(op,num1):
    
    def adder(num2):
        return num1 + num2
    
    def lower(num2):
        return num1-num2

    def multiplier(num2):
        return num1*num2

    def divisioner(num2):
        return num1/num2

    return eval(op)


def main(operation,number1,number2):
    switcher = {
               "add"    : "adder",
               "subs"   : "lower",
               "times"  : "multiplier",
               "divide" : "divisioner",
               }

    oper =  switcher.get(operation,"Operation no valid") 
    action = create_action(oper, number1)  
    print(action(number2))

if __name__ == "__main__":
    operation = args["operation"]
    number1 = int(args["num1"])
    number2 = int(args["num2"])
    main(operation,number1,number2)




