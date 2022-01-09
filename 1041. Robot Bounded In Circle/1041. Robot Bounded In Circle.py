class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        pos, head = (0, 0), 0

        for ch in instructions:
            if ch == "G":
                pos = (pos[0] + dirs[head][0], pos[1] + dirs[head][1])
            elif ch == "L":
                head = (head - 1) % 4
            else:
                head = (head + 1) % 4

        return pos == (0, 0) or head != 0


s = Solution()
instructions = "RLLGLRRRRGGRRRGLLRRR"
print(s.isRobotBounded(instructions))
