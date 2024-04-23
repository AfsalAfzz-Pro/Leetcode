class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        sorted_list = sorted(candies)
        greatest = sorted_list[-1]
        result_list = []
        for i in range(len(candies)):
            val = candies[i] + extraCandies
            print(val, candies[i], greatest)
            if val >= greatest:
                result_list.append(True)
            else:
                result_list.append(False)
        return result_list
        

s1 = Solution()
print(s1.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))