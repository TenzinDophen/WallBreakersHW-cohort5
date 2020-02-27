class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        return self.helper(nums, 0, len(nums)-1, target)
        
    def helper(self, nums, start, end, target):
        
        if start > end: 
            return -1
        
        mid = (end+start)//2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.helper(nums, start, mid-1, target)
        else:
            return self.helper(nums, mid+1, end, target)