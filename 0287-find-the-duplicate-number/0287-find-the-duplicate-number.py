class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        C = [0 for _ in range(n)]
        for i in range(n):
            C[nums[i]-1] += 1

        
        for i in range(n+1):
            if C[i] > 1:
                return i+1