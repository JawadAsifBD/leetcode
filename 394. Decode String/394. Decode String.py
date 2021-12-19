class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for char in s:
            if char!="]":
                stack.append(char)
            else:
                currStr = []
                num = []
                while stack and stack[-1].isalpha():
                    letter = stack.pop()
                    currStr = [letter] + currStr
                stack.pop()
                while stack and stack[-1].isdigit():
                    digit = stack.pop()
                    num = [digit] + num
                stack.append(int("".join(num)) * "".join(currStr))
            
        return "".join(stack)