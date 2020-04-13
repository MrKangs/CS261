'''
In this code sample we loop to n and do log(n) work
at every step of the way. This is a very common time for sorts.
'''

from timethis import timethis
import time

@timethis
def loop_and_split(i):
  for j in range (i):
    k = i
    while k > 1:
        k = k/2
        time.sleep(0.01) #We need to insert an arbitrary delay otherwise it is too fast

loop_and_split(2)
loop_and_split(4)
loop_and_split(8)
loop_and_split(16)
loop_and_split(32)