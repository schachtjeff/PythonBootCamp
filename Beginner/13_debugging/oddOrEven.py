# Debugging Odd or Even
'''
- Read the code in exercise.py - Spot the problems 🐞. 
- Modify the code to fix the program. 
Fix the code so that it works and passes the tests when you submit. 
'''

def odd_or_even(number):
    #ERROR -> if number % 2 = 0:
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
    
print(odd_or_even(3))
print(odd_or_even(2))