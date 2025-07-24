class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        alphabet_set = set()
        for al in sentence:
            if al.isalpha():
                alphabet_set.add(al.lower())
                if len(alphabet_set)==26:
                    return True
        return False   
      

    