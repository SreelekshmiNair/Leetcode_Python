class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pnt1 = 0;s=list(s);pnt2 = len(s)-1
        while pnt1 < pnt2:
            while pnt1<pnt2 and not (s[pnt1].isalnum()):
                pnt1+=1
            while  pnt1<pnt2 and not (s[pnt2].isalnum()):
                pnt2-=1
            if s[pnt1].lower()!=s[pnt2].lower():
                return False
            pnt1+=1
            pnt2-=1
        return True    
        