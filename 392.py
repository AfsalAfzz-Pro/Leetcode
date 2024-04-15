class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        flag_list = []
        for i in range(len(s)):
            for j in range(index, len(t)):
                if t[j] == s[i]:
                    flag = True
                    flag_list.append(flag)
                    index = j+1
                    break

        if len(flag_list) == len(s):
            return True
        return False
    
s1 = Solution()
print(s1.isSubsequence(s = "abc", t = "ahbgdc"))