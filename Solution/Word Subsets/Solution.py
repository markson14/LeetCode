class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        uni = collections.Counter()
        for b in B:
            for c,n in collections.Counter(b).items():
                # print(c,n)
                uni[c] = max(uni[c], n)
        res = []
        # print(uni)
        for a in A:
            count = collections.Counter(a)
            # print(count)
            if all(count[c] >= uni[c] for c in uni):
                res.append(a)
        return res
        