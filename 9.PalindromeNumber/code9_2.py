class Solution:
    def isPalindrome(self,x:int) -> bool:
        if x < 0 or (x != 0 and x % 10 ==0):
          #负数及整数
            return Fasle
        s = str(x)
        #字符串
        n = len(s)
        #字符串长度
        L, R = 0, n-1
        while L < R:
          #一一比较
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return Fasle
        else:
            return True
