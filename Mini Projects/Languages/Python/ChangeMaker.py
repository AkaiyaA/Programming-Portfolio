# Python Changemaker

# 1: SET UP
import random

print('This machine is going to make change.')
totalBalanceFlt = random.uniform(1,99)
totalBalanceFltRounded = round(totalBalanceFlt, 2)
print('Your total is: ' + str(totalBalanceFltRounded))
# -- Generates a random float balance, rounds it to two decimal places, and outputs it.

print('FOR DOLLARS: only put in standard bills, such as 1, 5, 10, 20, 50, and 100.')
print('FOR CHANGE: only put in standard coins, such as .01, .05, .10, and .25.')
moneyGiven = input('\nPlease input your combination of exact bills/coins, separating them by commas (","):\n')
# -- Takes in the dollar bill and coinage used.

moneyGivenList = moneyGiven.split(",")
# print(moneyGivenStrList)
moneyGivenFltList = [float(x) for x in moneyGivenList]
# print(moneyGivenIntList)
# -- Converts bill/s from a series of strings to a list of numbers to be calculated

# 2: DETERMINATION OF VALIDITY AND SUMMATION OF BILLS
for x in moneyGivenFltList:
    if x != 1 and x != 5 and x != 10 and x != 20 and x != 50 and x != 100:
        if x != .01 and x != .05 and x != .10 and x != .25:
            # Supposed to suggest "if this, AND if this," but I think it's janky and improperly formatted
            raise Exception("Invalid bill OR invalid change.")
            # -- This will stop the program if ANY "bill" or "coin" inserted is not within the standard bill parameters.

totalCash = sum(moneyGivenFltList)
# print(totalCash)
totalCashFlt = float(totalCash)
# print(totalCashFlt)
# -- This will continue the program, turning the sum into a float for proper rounding.

# 3: CALCULATION
totalChange = round((totalCashFlt - totalBalanceFltRounded), 2)
# -- Difference (change/remaining balance) is calculated and stored

# 4: RESULTS (CHANGE OR REMAINING BALANCE)
if totalChange > 0.0:
    print("$" + str(totalChange) + " is your change! Have a nice day!")
elif totalChange == 0.0:
    print("Perfect dollar amount! Have a nice day!")
else:
    while totalCashFlt < totalBalanceFltRounded:
        addedCash = input("Your remaining balance is: $" + str(totalChange) + ". Please input more money.\n")
        # More money inserted, one bill, coin, or many

        addedCashList = addedCash.split(",")
        addedCashIntList = [float(x) for x in addedCashList]
        # Takes list, if list is given, and turns them into numbers

        for x in addedCashIntList:
            if x != 1 and x != 5 and x != 10 and x != 20 and x != 50 and x != 100:
                if x != .01 and x != .05 and x != .10 and x != .25:
                    raise Exception("Invalid bill.")
                    # -- This will stop the program if ANY bill inserted is not within the standard bill parameters.

            else:
                totalAddedCash = sum(addedCashIntList)
                # -- This will continue the loop.

        # Essentially repeats the "determine validity and summation of bills" step

        totalCashFlt += totalAddedCash
        # print(str(totalCashFlt))
        # Adds separate bills together, takes that total and adds it to the total cash inserted, and outputs the new total

        totalChange = round((totalCashFlt - totalBalanceFltRounded), 2)
        # Recalculates the total change amount, and repeats loop.

    if totalChange > 0:
        print("$" + str(totalChange) + " is your change! Have a nice day!")
    elif totalChange == 0:
        print("Perfect dollar amount! Have a nice day!")

        # Completed Program!

# --------

# FUTURE NOTES:
# A. what about adding <1 change? I.e. add floats for better realism in both total balance AND user payment (basically 0.01 - 0.99) -- DONE, FINISHED 1/14/25
# B. better way of outputting an error when encountering "wrong" change (i.e. $24 bill)
# C. Can I add classes and functions to minimize the amount of code used? EX. instead of doing step two twice in the code, can I make one function that takes in parameters and process it the same way, and just call it both times?
# D. Removing the negative ("-") when the remaining balance is output?