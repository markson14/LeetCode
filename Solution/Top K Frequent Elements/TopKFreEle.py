def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_dict = {}
        for num in nums:
            if not num in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        nums_list = sorted(nums_dict.items(), key = lambda x:x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(nums_list[i][0])
        return res
        
if __name__ == '__main__':

    print (topKFrequent([1,1,1,2,2,3], 2))
    print (topKFrequent([1], 1))