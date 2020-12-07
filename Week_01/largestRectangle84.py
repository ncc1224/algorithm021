class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans

class Solution0:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n
        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans

class Solution0:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n<1:return 0
        if n<2:return heights[0]
        self.stack=[[-1,-1]]
        maxarea=0
        for i in range(n):
            if heights[i]>self.stack[-1][1]:
                self.stack.append([i,heights[i]])
            else:
                while self.stack[-1][1]>=heights[i] and self.stack[-1][0]!=-1: 
                    tmp = self.stack.pop()
                    m=tmp[1]*(i-self.stack[-1][0]-1)
                    maxarea=max(maxarea,m)
                self.stack.append([i,heights[i]])
        if self.stack[-1][0]>-1:
            bound=self.stack[-1][0]+1
        while self.stack[-1][0]!=-1:
            tmp = self.stack.pop()
            m=tmp[1]*(bound-self.stack[-1][0]-1)
            maxarea=max(maxarea,m)
        return maxarea

class Solution0:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n<1:return 0
        if n<2:return heights[0]
        self.stack=[-1]
        maxarea=0
        for i in range(n):
            if heights[i]>heights[self.stack[-1]]:
                self.stack.append(i)
            else:
                while heights[self.stack[-1]]>=heights[i] and self.stack[-1]!=-1: 
                    j = self.stack.pop()
                    m=heights[j]*(i-self.stack[-1]-1)
                    maxarea=max(maxarea,m)
                self.stack.append(i)
        if self.stack[-1]>-1:
            bound=self.stack[-1]+1
        while self.stack[-1]!=-1:
            j = self.stack.pop()
            m=heights[j]*(bound-self.stack[-1]-1)
            maxarea=max(maxarea,m)
        return maxarea
