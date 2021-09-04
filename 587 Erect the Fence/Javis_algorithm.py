class Solution:
    
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        
        def orientation(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    
        def inBetween(p: List[int], i: List[int], q: List[int]) -> bool:
            a = i[0] >= p[0] and i[0] <= q[0] or i[0] <= p[0] and i[0] >= q[0]
            b = i[1] >= p[1] and i[1] <= q[1] or i[1] <= p[1] and i[1] >= q[1]
            return a and b
        
        res = []

        # if the are less than four points.... take all the points
        if len(trees) < 4:
            return trees
        
        # find the leftmost point
        leftmost = trees[0]
        for point in trees:
            if point[0] < leftmost[0]:
                leftmost = point
                
        
        res.append(leftmost)
        p = leftmost
        
        # iterate over all the points and get convex hull points
        while True: 
            next_point = trees[(trees.index(leftmost)+1)%len(trees)]
            for point in trees:
                if orientation(p,point,next_point) < 0:
                    next_point = point
            
            # get in-line points
            for point in trees:
                if p is not point and next_point is not point and orientation(p,point,next_point) is 0\
                and inBetween(p,point,next_point):
                    res.append(point)
             
            p = next_point
            if p is leftmost:
                break
            res.append(next_point)
        
        return res
    
        
        