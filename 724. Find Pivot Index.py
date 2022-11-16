class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        sumsLeft = [0]*len(nums)
        sumsRight = [0]*len(nums)
        L = len(nums)
        sumsLeft[0] = int(nums[0])
        sumsRight[L-1] = int(nums[L-1])
        for i in range(1, len(nums)):
            sumsLeft[i] = int(sumsLeft[i - 1] + nums[i])
            sumsRight[L-1-i] = int(sumsRight[L-i] + nums[L-1-i])
        for i in range(len(nums)):
            if sumsLeft[i] == sumsRight[i]:
                return i
        return -1