class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        res = collections.Counter(words).items()
        res = sorted(res,key=lambda x:(-x[1],x[0]))
        return [i[0] for i in res][:k]
        