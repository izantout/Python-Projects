class Solution(object):
    def reverse(self, x):
        x2 = x
        y = 0
        z = 0

        while x > 0 or x < 0:
            z = abs(x) % 10
            y = y * 10 + z
            x = abs(x) // 10

        if x2 < 0:
            y = y * (-1)

        if -2**31 < y < (2**31)-1:
            y = y
        else:
            y = 0

        return(y)

        
        #Runtime: 28 ms, faster than 35.83% of Python online submissions for Reverse Integer.
        #Memory Usage: 13.3 MB, less than 88.89% of Python online submissions for Reverse Integer.
