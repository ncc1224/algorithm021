class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums,0,len(nums)-1)
    def mergeSort(self,nums,left,right):
        if left>=right:return 0
        mid=left+(right-left)//2
        cnt=self.mergeSort(nums,left,mid)+self.mergeSort(nums,mid+1,right)
        temp=[0]*(right-left+1)
        j,t,k=mid+1,mid+1,0
        for i in range(left,mid+1):
            while t<=right and nums[i]/2.0>nums[t]:t+=1
            cnt += t-(mid+1)
            while j<=right and nums[i]>nums[j]:
                temp[k]=nums[j]
                k+=1
                j+=1
            temp[k]=nums[i]
            k+=1
        while j<=right:
            temp[k]=nums[j]
            k+=1
            j+=1
        nums[left:right+1]=temp
        return cnt
