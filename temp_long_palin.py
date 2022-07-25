class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        tmp_len = 0
        max_len = 0
        max_palin = s
        for i in range(len_s-1):
            for j in range(i+1, len_s+ 1):
                if self.check_palin(s[i:j]):
                    tmp_len = len(s[i:j])
                    if tmp_len > max_len:
                        max_len = tmp_len
                        max_palin = s[i:j]
        return max_palin
    def check_palin(self,s:str) -> str:
        if s == "" or len(s)==1:
            return True
        if s[0] == s[-1]:
            return self.check_palin(s[1:-1])
        return False
