'''
Here we sort a list using a very basic but intuitive method
we loop through it onece for every element, we then move
elements over one at a time until they are bigger than
the element on the left but smaller than the element on the right.
'''

from timethis import timethis
import random

@timethis
def bubble(arr):
    l = len(arr)        
    for a in range(l):
        for b in range(l-1):
            if (arr[a] < arr[b]):
                arr[a], arr[b] = arr[b], arr[a]
    return arr 

'''
We generate randomly sorted lists of various sizes then sort them.
'''


for i in [250,500,1000,2000,4000]:
    my_list = [random.randint(0,i) for x in range(i)]
    bubble(my_list)