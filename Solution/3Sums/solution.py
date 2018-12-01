class Solution1:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        time: 1448 ms
        hashtable 
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return list(map(list, res))

class Solution2:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        time: 1152ms
        two pointer
        """
        nums = sorted(nums)
        res = []
        if len(nums) < 3:
            return res
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        return res
