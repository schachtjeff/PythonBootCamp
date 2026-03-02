#Debugging Leap year
'''
- Read the code

- Spot the problems 🐞.

- Modify the code to fix the program.   


Fix the code so that it works and when you hit submit it should pass all the tests. 


This is how you work out whether if a particular year is a leap year.


- on every year that is divisible by 4 with no remainder

- except every year that is evenly divisible by 100 with no remainder

- unless the year is also divisible by 400 with no remainder
'''

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            #Error -> if year % 4000 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False