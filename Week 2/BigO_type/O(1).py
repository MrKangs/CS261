'''
This will insert into an empty list at different indexes.
Make sure to run it a few times to see the output. Sometimes
Repl.it will have a hiccup and take longer to run a particular
function.
'''

from timethis import timethis
import time

@timethis
def insert_at_n(l,n):
    l[n] = "Hello"

my_list = [None] * 10000000 #Create empy list of 10 million

insert_at_n(my_list, 100)
insert_at_n(my_list, 10000)
insert_at_n(my_list, 1000000)