'''
We end with the fibonacci sequence implemented recursively.
At every stage it creates two additional recursive calls. Those calls
then make two more calls, and each of those make two more till they
hit the base case.
'''

from timethis import timethis

# Due to the recursive call we need to time a helper function

@timethis
def fibcaller(number):
    fibonacci(number)

def fibonacci(number):
    if number == 0: return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)

fibcaller(5)
fibcaller(10)
fibcaller(20)
fibcaller(30)