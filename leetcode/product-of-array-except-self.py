class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix_arr = [1] * len(nums)
        suffix_arr = [1] * len(nums)

        for i in range(1,len(nums)):
            prefix_arr[i] = nums[i-1] * prefix_arr[i-1]

            
        for j in range(len(nums)-2,-1,-1):
            suffix_arr[j] = nums[j+1] * suffix_arr[j+1]

        without_self = [0]*len(nums)
        for val in range(0, len(nums)):
            without_self[val] = suffix_arr[val] * prefix_arr[val]

        return without_self