class Solution1(object):
    def levelOrder(self, root):
        levels = [[root] if root else []]
        while levels[-1]:
            levels.append([child for node in levels[-1] for child in node.children])
        return [[node.val for node in level] for level in levels[:-1]] 
class Solution1(object):
    def levelOrder(self, root):
        q, ret = [root], []
        while any(q):
            ret.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ret
class Solution1:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:return []
        ret=[]
        pre=[root]
        def dfs(node,level):
            if len(ret)==level:
                ret.append([])
            ret[level].append(node.val)
            for c in node.children:
                dfs(c,level+1)

        dfs(root,0)
        return ret
