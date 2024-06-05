class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n # 길이가 i인 배열의 최대 부분 배열 합을 저장하는 배열

        # 첫 번째 원소 처리
        dp[0] = nums[0]

        # 나머지 원소 처리
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])

        # 최대 값 찾기
        return max(dp)