class Solution:
    def compressedString(self, word: str) -> str:
        low = 0
        high = 0
        output = ""
        while low < len(word):
            if high > len(word) - 1:
                break
            if word[low] == word[high]:
                if high - low== 9:
                    output += "9" + word[low:low+1]
                    low = high

                else:
                    high += 1
            else:
                count = high - low
                output += str(count) + word[low:low+1]
                low = high

        count = high - low
        output += str(count) + word[low:low+1]
        return output

solution = Solution()
word = "abcde"
#word = "aaaaaaaaaaaaaabb"
solution.compressedString(word)

