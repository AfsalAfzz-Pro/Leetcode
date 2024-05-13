class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)//2
        a = s[:n]
        b = s[n:]

        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        
        def check_vowel(string):
            count = 0
            for char in string:
                if char in vowels:
                    count += 1
            return count

        a_vowels = check_vowel(a)
        b_vowels = check_vowel(b)

        if a_vowels == b_vowels:
            return True
        else:
            return False
        

s1 = Solution()
print(s1.halvesAreAlike("book"))