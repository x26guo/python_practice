class Solution:
    def minLength(self, s: str) -> int:
        output = []
        for i in range(len(s)):
            if len(output) > 0:
                if s[i] == 'B' and output[len(output) - 1] == 'A':
                    del output[len(output) - 1]
                elif s[i] == 'D' and output[len(output) - 1] == 'C':
                    del output[len(output) - 1]
                else:
                    output.append(s[i])
            else:
                output.append(s[i])
        return len(output)