class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        start = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]+1:
                if start == nums[i-1]:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{nums[i - 1]}")
                start = nums[i]

        if start == nums[-1]:
            ranges.append(str(nums[i-1]))
        else:
            ranges.append(f"{start}->{nums[i-1]}")
          
        return ranges