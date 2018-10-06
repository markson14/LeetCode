class Solution:
    """
    Two Pointer
    Time Complexity: O(N)
    Space Complexity: O(1)

    Algorithm

    For a starting index base, let's calculate the length of the longest mountain A[base], A[base+1], ..., A[end].

    If such a mountain existed, the next possible mountain will start at base = end; 
    if it didn't, then either we reached the end, or we have A[base] > A[base+1] and we can start at base + 1.   
    """
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = base = 0
        n = len(A)
        while base < n:
            end = base
            if end+1 < n and A[end] < A[end+1]:
                while end+1 < n and A[end] < A[end+1]:
                    end += 1
            
                if end+1 < n and A[end] > A[end+1]:
                    while end+1<n and A[end] > A[end+1]:
                        end += 1
                    
                    ans = max(ans, end-base+1)
            
            base = max(end, base+1)
        return ans
            
                
        