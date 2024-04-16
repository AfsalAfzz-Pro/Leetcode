class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        one = [list((k,v)) for k,v in frequency.items() if v == 1]
        return one[0][0]
    
s1 = Solution()
print(s1.singleNumber([4,1,2,1,2]))