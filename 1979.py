class Solution:
    def findGCD(self, nums: list[int]) -> int:
        sorted_list = sorted(nums)
        mn = sorted_list[0]
        mx = sorted_list[-1]
        div_list = []
        for i in range(1,mn+1):
            if mn % i == 0 and mx % i== 0:
                div_list.append(i)
        return div_list[-1]
        

s1 = Solution()
print(s1.findGCD([2,5,6,9,10]))