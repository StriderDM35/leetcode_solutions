class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        used = {}
        for i, value in enumerate(nums):
            num_1 = nums[i]
            remain = target - num_1
            
            if remain in used:
                return[i, used[remain]]

#Solution obtainec from https://www.code-recipe.com/post/two-sum as I was using two for loops initially 
#   which resulted in "Time Limit Exceeded"
#This solution is a lot faster as it only uses one for loop
#Runtime: 73 ms
#Memory usage: 14.2 MB