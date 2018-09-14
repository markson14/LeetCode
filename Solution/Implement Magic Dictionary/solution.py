class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.save = []

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.save = dict
        return

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        c = 0
        for i in self.save:
            if len(i) == len(word):
                for j in range(len(i)):
                    if not i[j] == word[j]:
                        c+=1
            if c == 1:
                return True
            else:
                c = 0
        return False
