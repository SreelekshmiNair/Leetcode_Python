class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        alphabet_set = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        for al in sentence:
            if al.lower() in alphabet_set:
                alphabet_set.remove(al.lower())
        return len(alphabet_set)==0
      

    