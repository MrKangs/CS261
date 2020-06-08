# word_count.py
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. The word
# counter will return the top X words, as indicated
# by the user.
# Name: Kenneth Kang
# Date: 6-8-2020
# ===================================================

import re
from hash_map import HashMap

"""
This is the regular expression used to capture words. It could probably be endlessly
tweaked to catch more words, but this provides a standard we can test against, so don't
modify it for your assignment submission.
"""
rgx = re.compile("(\w[\w']*\w|\w)")

def hash_function_2(key):
    """
    This is a hash function that can be used for the hashmap.
    """

    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash

def top_words(source, number):
    """
    Takes a plain text file and counts the number of occurrences of case insensitive words.
    Returns the top `number` of words in a list of tuples of the form (word, count).

    Args:
        source: the file name containing the text
        number: the number of top results to return (e.g. 5 would return the 5 most common words)
    Returns:
        A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """

    keys = set()

    ht = HashMap(2500,hash_function_2)

    # This block of code will read a file one word as a time and
    # put the word in `w`. It should be left as starter code.
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            for w in words:
                # Change all words into lower case since we are saying that "the" = "THE"
                w = w.lower()

                # If the key value already exists, then update the count
                if ht.contains_key(w) == True:
                    ht.put(w, ht.get(w) + 1)
                
                # Else, add into the bucket and update the set for keys
                else:
                    ht.put(w, 1)
                    keys.add(w)

    # Set an empty array to added the top (user input number value) word frequency
    sortedList = []

    # Going to append (user input number value) into the array
    for i in range(number):

        # Set it equal to 0 as initializie 
        topValue = 0

        # Will look all over the key values in the keys set and compare to the current highest count
        for key in keys:
            if(ht.get(key) > topValue):
                topKey = key
                topValue = ht.get(key)

        # Once we are done with comparing values, remove it from both bucket and key list that we don't need to compare again
        ht.remove(topKey)
        keys.remove(topKey)

        # Add to the sorted list 
        sortedList.append((topKey, topValue))
    
    # Return the full list once the loop is complete 
    return (sortedList)
            


print(top_words("D:\CS261\Assignment 5 Hash Map Implementation of a Concordance\Concordance\\alice.txt",10))  # COMMENT THIS OUT WHEN SUBMITTING TO GRADESCOPE