class Solution:
    def smallestNumber(self, pattern: str) -> str:
        output = []
        stack = []

        for n in range (len(pattern) + 1):
            stack.append(n + 1)

            while stack and (n == len(pattern) or pattern[n] == 'I'):
                output.append(str(stack.pop()))
        return "".join(output)
