'''
This loop does O(n) by summing all the numbers in a list.
'''

from timethis import timethis

@timethis
def sum_list(l):
    total = 0
    for i in l:
        total = total + i

'''
Here we first make lists of various sizes so they don't
affect the run time of the summing then we time just time
just the list summing function.
'''

for i in [10000,20000,40000,80000,160000,320000]:
    my_list = [x for x in range(i)]
    sum_list(my_list)