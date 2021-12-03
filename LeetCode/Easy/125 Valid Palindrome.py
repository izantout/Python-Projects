class Solution(object):
    def isPalindrome(self, s):
        import re
        """
        :type s: str
        :rtype: bool
        """
        f = (re.sub("[^0-9a-zA-Z]","",s)).lower()
        n = f[::-1]
        if f == n:
            return True
        else:
            return False
