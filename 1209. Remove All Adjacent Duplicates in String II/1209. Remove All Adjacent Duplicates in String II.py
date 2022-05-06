class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque()  # list works fine too
        for ch in s:
            # current character belongs to the previous substring
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:  # k-length substring reached, remove substring
                    _ = stack.pop()
            else:  # current character is its own substring
                stack.append([ch, 1])
        # concatenate remaining substrings
        return ''.join(ch*n for ch, n in stack)
