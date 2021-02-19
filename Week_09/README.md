通配符匹配
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_cur,p_cur,match,star = 0,0,0,-1
        while s_cur<len(s):
            if p_cur< len(p) and (s[s_cur]==p[p_cur] or p[p_cur]=='?'):
                s_cur,p_cur = s_cur + 1,p_cur + 1
            elif p_cur<len(p) and p[p_cur]=='*':
                match,star,p_cur = s_cur,p_cur,p_cur+1
            elif (star!=-1):
                p_cur,match = star+1,match+1
                s_cur = match
            else:return False
        while p_cur<len(p) and p[p_cur]=='*':p_cur = p_cur+1
        return p_cur==len(p)
