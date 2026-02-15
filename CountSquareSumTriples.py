'''
A square triple (a,b,c) is a triple where a, b, and c are integers and a^2 + b^2 = c^2.
Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.
'''

import math

class Solutions(object):
    def countTriples(self, n):
        
        result = 0
        
        for i in range(1, n+1):
            for j in range(i, n+1):
                sum = math.sqrt(i*i + j*j)
                if int(sum) == sum and sum <= n:
                    result += 2
        return result
    
    