class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:return -1
        left,right=0,len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]:
                if target>=nums[left] and target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if target<=nums[right] and target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:return -1
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo if target== nums[lo] else -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(l,r):
            if l > r:
                return -1
            m = (r+l)//2
            if nums[m] == target:
                return m
            # follow left half if it is sorted and target is in its range or if right half is sorted but target is not in its range
            if nums[l] <= target < nums[m] or (nums[m] <= nums[r]  and not nums[m] < target <= nums[r]):
                return helper(l,m-1)
            else: 
                return helper(m+1, r)
        return helper(0,len(nums)-1)
