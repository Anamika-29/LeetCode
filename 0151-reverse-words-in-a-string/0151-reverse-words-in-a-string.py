class Solution:
    def reverseWords(self, s):
        s = list(" ".join(s.split()))[::-1]
        i = 0 
        while i < len(s):
            start = i 
            while i < len(s) and not s[i].isspace():
                i += 1
            self.reverse(s, start, i-1)
            i += 1
        return "".join(s)

    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1; j -= 1
