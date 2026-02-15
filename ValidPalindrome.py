'''
A phrase in a palindomre if, after converting all uppercase letters into lowercase letters and ramoving all non-alphanumeric
characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, of false otherwise.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = s.casefold()
        s = ''.join(c for c in s if c.isalnum())
        for i in range(len(s) // 2):
            if s[i] != s[-1-i]:
                return False
        return True
        