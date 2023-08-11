class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=False
        if x<0:
            x=x*-1
            flag=True
        n=str(x)
        n=n[::-1]
        x=int(n)
        if x>(2**31)-1:
            return 0
        if flag:
            x=x*-1
        return x
        
        