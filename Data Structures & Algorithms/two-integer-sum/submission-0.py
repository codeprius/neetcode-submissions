class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       s={}
       for i,j in enumerate(nums):
        if j in s:
            return[s[j],i]
        s[target-j]=i
