class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        list1 = [str(n) for n in str(x)]
        list2 = [str(n) for n in str(x)]
        list2.reverse()

        if list1 == list2:
            return True
        else:
            return False

        
            #Runtime: 76 ms, faster than 36.40% of Python online submissions for Palindrome Number.
            #Memory Usage: 13.6 MB, less than 13.32% of Python online submissions for Palindrome Number.
