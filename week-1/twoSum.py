class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            search = target-n
            if search in dic:
                return [dic[search], i]
            dic[n] = i