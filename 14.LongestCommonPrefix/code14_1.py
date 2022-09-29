class Solution:
    def longestCommonPrefix(self,strs: list[str]) -> str:
        res = ""
        #初始化res

        for i in range(len(strs[0])):
          #对strs中的第一个单词的所有字母遍历
            for s in strs:
              #与strs中的所有单词匹配
                if i == len(s) or s[i] != strs[0][i]:
                  #防止i溢出
                    return res
            res += strs[0][i]
            #更改res

        return res
