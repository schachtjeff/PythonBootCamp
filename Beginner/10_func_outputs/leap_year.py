#Leap Year Program
#Overview: Find out if the year is a leap year.
'''
This is how you work out whether if a particular year is a leap year. 

- on every year that is divisible by 4 with no remainder

- except every year that is evenly divisible by 100 with no remainder 

- unless the year is also divisible by 400 with no remainder  
'''
def is_leap_year(year) -> bool:
    # if the year is divisible by 4, no remainder.
    if year % 4 == 0:
        print("passes the 4 years test")
        # not divisible by 100
        if year % 100 != 0:
            print("passes the 100 years test and is a Leap Year")
            return True
        else:
            if year % 400 == 0:
                print("passes the 400 years test and is a Leap year")
                return True
    return False

print(is_leap_year(2100))
print(is_leap_year(2000))