'''
Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from
'a' to 'z' between word1 and word2 is at most 3.
Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.
The frequency of a letter x is the number of times it occurs in the string.
'''

import collections

class Solution(object):
    def CheckAlmostEquivalent(self, word1, word2):
        
        data1 = collections.Counter(word1)
        data2 = collections.Counter(word2)
        
        for element in "abcdefghijklmnopqrstuvwxyz":
            if abs(data1[element] - data2[element]) > 3:
                return False
        return True