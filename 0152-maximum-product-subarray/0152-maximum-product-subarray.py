class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        currentMax = nums[0]
        currentMin = nums[0]
        prodMax = nums[0]

        for i in range(1, len(nums)):
            vals = (nums[i], currentMax*nums[i], currentMin*nums[i])
            currentMax = max(vals)
            currentMin = min(vals)

            prodMax = max(currentMax, prodMax)

        return prodMax
        