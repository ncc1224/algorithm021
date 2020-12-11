class Solution1:  #小顶堆方式
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        stat=collections.Counter(nums)
        stat=list(stat.items())
        def sift_up(h,j):
            p=(j-1)//2
            while p>=0 and heap[p][1]>heap[j][1]:
                heap[p],heap[j]=heap[j],heap[p]
                j=p
                p=(j-1)//2
        def sift_down(h,j):
            left=2*j+1   #index from 0
            right=2*j+2
            while right<len(heap) and (heap[left][1]<heap[j][1] or heap[right][1]<heap[j][1]):
                if heap[left][1]<heap[right][1]:
                    heap[left],heap[j]=heap[j],heap[left]
                    j=left
                else:
                    heap[right],heap[j]=heap[j],heap[right]
                    j=right
                left=2*j+1
                right=2*j+2
            if left<len(heap) and heap[left][1]<heap[j][1]:
                heap[left],heap[j]=heap[j],heap[left]
        
        for i in range(k):
            heap.append(stat[i])
            sift_up(heap,len(heap)-1)
        for i in range(k,len(stat)):
            if heap[0][1] < stat[i][1]:
                heap[0]=stat[i]
                sift_down(heap,0)
        return [item[0] for item in heap]

class Solution:  #快排思想
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k<1:return []
        stat=collections.Counter(nums)
        stat=list(stat.items())

        def partition(lis,low,high):
            v = lis[low]
            left=low
            right=high
            while left<right:
                while left<right and lis[right][1]<=v[1]:
                    right -=1
                lis[left]=lis[right]
                while left<right and lis[left][1]>v[1]:
                    left +=1
                lis[right]=lis[left]
            lis[left]=v
            return left
        def partition2(lis,low,high):
            v = lis[high]
            left=low
            right=low
            for right in range(low,high):
                if lis[right][1]>v[1]:
                    lis[right],lis[left]=lis[left],lis[right]
                    left+=1
            lis[high],lis[left]=lis[left],lis[high]
            return left
        def partition3(lis,low,high):
            v = lis[low]
            left=high
            right=high
            for left in range(high,low,-1):
                if lis[left][1]<v[1]:
                    lis[right],lis[left]=lis[left],lis[right]
                    right-=1
            lis[low],lis[right]=lis[right],lis[low]
            return right
        start,end = 0,len(stat)-1
        index = partition(stat,start,end)
        while index!=k-1:
            if index<k-1:
                start=index+1
            else:
                end=index-1
            index = partition(stat,start,end)
        return [item[0] for item in stat[:k]]
