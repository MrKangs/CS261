"""
@@ CS 261 Assignment 5 - HashMap SpellChecker Tester
@@ Solution Test Script
@author: Martin Edmunds
"""

"""Change this import depending on spellchecker file name"""
from word_count import top_words
from gradescope_utils.autograder_utils.decorators import weight
import unittest
import re

rgx = re.compile("(\w[\w']*\w|\w)")
source = "alice.txt"


# Helper function that returns a (key, value) sorted list of (words, count)
# Found from a source file.
# Args:
#   source - the text file to search
#   number - number of 2-tuple results to return
# Return:
#   (key, value) sorted (highest values first) list
def get_top_words_standard(source, number):
    standard_map = {}
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            for w in words:
                lw = w.lower()
                if lw in standard_map:
                    standard_map[lw] = standard_map[lw] + 1
                else:
                    standard_map[lw] = 1

    totals = []
    keys = standard_map.keys()
    for key in keys:
        # get value, key pair
        totals.append((standard_map[key], key))
    # totals = (value, key) list
    # sort by value
    totals = sorted(totals, reverse=True)
    for i in range(len(totals)):
        totals[i] = (totals[i][1], totals[i][0])
    # totals = (key, value) sorted by value

    return totals[:number]


# Class for testing the student spell checker, checks against the standardized Python Dictionary
class TestStudentWords(unittest.TestCase):
    @weight(15)
    def test_top_words_1(self):
        """Tests that the top word returned matches the standard results"""
        num_of_results = 1
        standard_results = get_top_words_standard(source, num_of_results)
        results = top_words(source, num_of_results)
        words = []
        standard_words = []
        for key, value in standard_results:
            standard_words.append(key)
        for key, value in results:
            words.append(key)
        # check that the student hash map returns the exact list as the python dict
        self.assertTrue(words == standard_words)

    @weight(6)
    def test_top_words_3(self):
        """Tests that the top three words returned matches the standard results"""
        num_of_results = 3
        standard_results = get_top_words_standard(source, num_of_results)
        results = top_words(source, num_of_results)
        words = []
        standard_words = []
        for key, value in standard_results:
            standard_words.append(key)
        for key, value in results:
            words.append(key)
        # check that the student hash map returns the exact list as the python dict
        self.assertTrue(words == standard_words)

    @weight(9)
    def test_top_words_5(self):
        """Tests that the top five words returned matches the standard results"""
        num_of_results = 5
        standard_results = get_top_words_standard(source, num_of_results)
        results = top_words(source, num_of_results)
        words = []
        standard_words = []
        for key, value in standard_results:
            standard_words.append(key)
        for key, value in results:
            words.append(key)
        # check that the student hash map returns the exact list as the python dict
        self.assertTrue(words == standard_words)


# Class for testing the student spell checker: Checks the counts of words returned
class TestStudentWordCount(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """Running the HashMap and dictionary functions once to build the results needed for grading"""
        num_of_results = 5
        self.standard_results = get_top_words_standard(source, num_of_results)
        self.results = top_words(source, num_of_results)
        self.counts = []
        self.standard_counts = []
        for key, value in self.standard_results:
            self.standard_counts.append(value)
        for key, value in self.results:
            self.counts.append(value)

    @weight(2)
    def test_top_word_count_1(self):
        """Test that the top word returned matches the standard count"""
        # check that the student hash map returns the exact list as the python dict
        self.assertTrue(self.counts[0] == self.standard_counts[0])

    @weight(1)
    def test_top_word_count_3_a(self):
        """Test that the 1st place of the top 3 returned matches the standard count"""
        self.assertTrue(len(self.counts) >= 3)
        self.assertTrue(self.counts[0] == self.standard_counts[0])

    @weight(1)
    def test_top_word_count_3_b(self):
        """Test that the 2nd place of the top 3 returned matches the standard count"""
        self.assertTrue(len(self.counts) >= 3)
        self.assertTrue(self.counts[1] == self.standard_counts[1])

    @weight(1)
    def test_top_word_count_3_b(self):
        """Test that the 3rd place of the top 3 returned matches the standard count"""
        self.assertTrue(len(self.counts) >= 3)
        self.assertTrue(self.counts[2] == self.standard_counts[2])

    @weight(1)
    def test_top_word_count_5_a(self):
        """Test that the 1st place of the top 5 returned matches the standard count"""
        self.assertTrue(len(self.counts) >= 5)
        self.assertTrue(self.counts[0] == self.standard_counts[0])

    @weight(1)
    def test_top_word_count_5_b(self):
        """Test that the 2nd place of the top 5 returned matches the standard count"""
        self.assertTrue(len(self.counts) >= 5)
        self.assertTrue(self.counts[1] == self.standard_counts[1])

    @weight(1)
    def test_top_word_count_5_c(self):
        """Test that the 3rd place of the top 5 returned matches the standard count"""
        self.assertTrue(len(self.counts) >= 5)
        self.assertTrue(self.counts[2] == self.standard_counts[2])

    @weight(1)
    def test_top_word_count_5_d(self):
        """Test that the 4th place of the top 5 returned matches the standard count"""
        self.assertTrue(len(self.counts) >= 5)
        self.assertTrue(self.counts[3] == self.standard_counts[3])

    @weight(1)
    def test_top_word_count_5_e(self):
        """Test that the 5th place of the top 5 returned matches the standard count"""
        self.assertTrue(len(self.counts) >= 5)
        self.assertTrue(self.counts[4] == self.standard_counts[4])


if __name__ == '__main__':
    unittest.main()

