class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        # handle number
        num = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            elif s[i] == "*" or s[i] == "/" or s[i] == "+" or s[i] == '-':
                stack.append(num)
                stack.append(s[i])
                num = 0
            else:
                num = num * 10 + int(s[i])
            i += 1
        stack.append(num)

        # handle * and /
        stack2 = []
        i = 0
        while i < len(stack):
            val = stack[i]
            if val == "*":
                i1 = stack2.pop()
                i2 = stack[i+1]
                product = i1 * i2
                stack2.append(product)
                i += 2
            elif val == "/":
                i1 = stack2.pop()
                i2 = stack[i+1]
                divide = i1 // i2
                stack2.append(divide)
                i+=2
            else:
                stack2.append(val)
                i+=1
        # handle + and -
        positive = not (stack2[0] == "-")
        if positive:
            result = int(stack2[0])
            i = 1
        else:
            result = (-int(stack2[1]))
            i = 2
        while i < len(stack2):
            if stack2[i] == "+":
                result = result + int(stack2[i + 1])
            elif stack2[i] == "-":
                result = result - int(stack2[i + 1])
            i += 2
        return result

solution = Solution()
s ="4/3+2"
solution.calculate(s)