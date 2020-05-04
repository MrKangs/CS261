

def binarySearch(arr, x): 
    # start with the entire array 
    low = 0
    high = len(arr)-1
    found = -1
    index = 0
   
    # repeatedly subdivide the array into half
    while low <= high:  
      # find the midpoint of the sequence
      mid = (low + high) // 2;     
        # does the midpoint contain the query value?
      if arr[mid] == x:
            found = mid 
            index = mid
            return found, index 
  
        # does the query value precede the midpoint?
      elif x < arr[mid] : 
            high = mid - 1
            
        # or does the query value follow the midpoint?
      else: 
            low = mid + 1
              
    # If we reach here, then the query value is not in the array 
      index = low  
    return  found, index
  
# Driver Code 
found, index = binarySearch([2,7,9,11,14,16],7)  

if (found == -1):
  print ("value should be inserted at index =", index)
else:
  if (found != -1):
   print("value found at index =", index)
