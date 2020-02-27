class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        if not nums: return 0
        
        if len(nums)==1: return nums[0]
        
        if len(nums)==2: return max(nums[0],nums[1])
        
        #[1,2,3,1]
        def robber(nums):
            
            current=prev=0
            
            for num in nums:
                #[2,3,1], [1,2,3]
                
                current,prev=max(current,prev+num),current
                
            return current
        
        return max(robber(nums[1:]),robber(nums[:-1]))