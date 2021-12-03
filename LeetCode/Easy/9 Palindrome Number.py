class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        list1 = [str(n) for n in str(x)] # Converts integer to string then adds each digit to list
        list2 = [str(n) for n in str(x)] # Creates another list equal to the first
        list2.reverse() # Reverses created list

        if list1 == list2: # Checks if lists are equal
            return True
        else:
            return False

        
            #Runtime: 76 ms, faster than 36.40% of Python online submissions for Palindrome Number.
            #Memory Usage: 13.6 MB, less than 13.32% of Python online submissions for Palindrome Number.
