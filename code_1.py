#暴力枚举法
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        #数组长度
        for i in range(n):
            for j in range(i+1,n):
                #只需要和后面的数匹配，前面的数在前一轮中已经匹配过
                if (nums[i]+nums[j]==target):
                    return[i,j]
        return[]
