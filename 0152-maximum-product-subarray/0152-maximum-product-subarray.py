class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 최대 곱과 최소 곱을 저장
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            # 현재 요소가 음수인 경우, 최소 곱을 업데이트해야 함
            # 왜냐하면 음수와 음수를 곱하면 양수가 될 수 있기 때문
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(result, max_so_far)

        return result
