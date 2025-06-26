class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n <0 :
            ns = -1
            n = -n
        else:
            ns = 1
        ans = 1
        while n:
            if n%2 ==0:
                x = x*x
                n = n//2
            else:
                ans = ans * x
                n -= 1

        if ns>0:
            return ans
        else:
            return 1/ans