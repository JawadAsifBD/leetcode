class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        sw1 = [0]*26
        sw2 = [0]*26
        for i in range(len(s1)):
            sw1[ord(s1[i])-ord('a')] += 1
            sw2[ord(s2[i])-ord('a')] += 1

        for i in range(len(s2)-len(s1)):
            if sw1 == sw2:
                return True
            sw2[ord(s2[i+len(s1)])-ord('a')] += 1
            sw2[ord(s2[i])-ord('a')] -= 1
        return sw1 == sw2


s = Solution()
s1 = "adc"
# s2 = "eidboaoo"
s2 = "dcda"
print(s.checkInclusion(s1, s2))
