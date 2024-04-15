class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        count = 0
        for word in words:
            index = 0
            for char in word:
                # Find the index of the current character in s
                index = s.find(char, index)
                if index == -1:
                    break  # If the character is not found in s, word is not a subsequence
                index += 1  # Move the index to the next position for the next character
            else:
                count += 1  # Increment count only if all characters of word are found in s
        return count
    
s1 = Solution()
print(s1.numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))