class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
      #将整数转换为字符串并与反转字符串比较
