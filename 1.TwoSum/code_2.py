#哈希表
class Solution:
    def twoSum(self,nums:list[int],target:int)->list[int]:
        hashtable=dict()
        #创建哈希表
        for i,num in enumerate (nums):
            #对遍历的nums数组标出数据和数据下标
            if target -num in hashtable :
                #如果匹配成功
                return [hashtable [target -num],i]
                #输出下标组合
            hashtable [nums[i]]=i
            #如果匹配失败，将数组中的数字放入哈希表中
        return[]
