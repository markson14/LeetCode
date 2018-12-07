class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNsum(l,r,target,N,result,res):
            if r-l+1 < N or N<2 or target < nums[l]*N or target > nums[r]*N:  # early termination which is the key point to reduce time complexity
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        res.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], res)
        nums.sort()
        res = []
        findNsum(0,len(nums)-1,target,4,[],res)
        return res



class Solution2:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-3):
            cur1 = target
            if i != 0 and nums[i] == nums[i-1]:
                continue
            cur2 = cur1 - nums[i]
            for j in range(i+1,n-2):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                cur3 = cur2 - nums[j]
                left = j+1
                right = n-1
                ###############################################
                
                """
                    early termination是缩短时间的关键，从超时到130ms
                """
                if cur3 < nums[left]*2 or cur3 > nums[right]*2:
                    continue
                ###############################################
                while left < right:
                    if nums[left]+nums[right] == cur3:
                        # print(nums)
                        # print(i,j,left,right)
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]: left += 1
                        while left < right and nums[right] == nums[right+1]: right -= 1
                    elif nums[left]+nums[right] > cur3:
                        right -= 1
                    else:
                        left += 1
        return res