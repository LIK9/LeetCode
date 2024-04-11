class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # res = 0
        # for n in nums:
        #     res = res ^ n
        # return res
        nums.sort()
        print(nums)
        i = 0
        while i < len(nums):
            if i == len(nums)-1 or nums[i] != nums[i+1]:
                return nums[i]
            else:
                i += 2