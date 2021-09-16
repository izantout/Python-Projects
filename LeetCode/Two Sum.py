class Solution(object):
    def twoSum(self, nums, target):
        nums2 = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    nums2.append(i)
                    nums2.append(j)
                    return(nums2)
                    nums2.remove(i)
                    nums2.remove(j)
                else:
                    continue
