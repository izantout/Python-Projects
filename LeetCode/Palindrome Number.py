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
