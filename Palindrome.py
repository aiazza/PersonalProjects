# Leetcode problem : https://leetcode.com/problems/palindrome-number/
# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


class Solution():
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        fowardstring = []
        backwardstring =[]
        for i in str(x):
            str(fowardstring.append(i))
        for i in reversed(str(x)):
            str(backwardstring.append(i))
        print(fowardstring, backwardstring)
        if fowardstring == backwardstring:
            return True
        else:
            return False

C = Solution()

print(C.isPalindrome(x=123))