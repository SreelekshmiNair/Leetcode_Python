class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        #2 pointer approach after converting to list
        ls = list(s)   
        pnt1 = 0; pnt2 = len(ls)-1; str1 = 'aeiouAEIOU' 
           
        while(pnt1<pnt2):
            if ls[pnt1] in str1 and ls[pnt2] in str1:
                ls[pnt1],ls[pnt2] = ls[pnt2],ls[pnt1]
                pnt1+=1;pnt2-=1
            elif ls[pnt1] not in str1:
                pnt1+=1
            elif ls[pnt2] not in str1:
                pnt2-=1
        return ''.join(ls)