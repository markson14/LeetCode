class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A = sorted(map(abs,A))
        # print(A)
        n = len(A)//2
        counter = collections.Counter(A)
        if counter[0] % 2 != 0:
            return False
        counter_s = sorted(counter.items(), key = lambda x:x[0])
        for i in range(len(counter)-1,-1,-1):
            # print(i)
            right = counter_s[i][0]
            left = counter_s[i][0] / 2
            if left in counter:
                counter[left] -= counter[right]
                counter[right] = 0
        # print(counter)
        for i in counter:
            if counter[i] != 0:
                return False
        return True