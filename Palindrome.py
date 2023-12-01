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