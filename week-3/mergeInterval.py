class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key = lambda x: x[0])
        
        stack = []
        
        for i in intervals:
            start = i[0]
            end = i[1]
            if stack:
                p = stack.pop()
                pst = p[0]
                pend = p[1]
                if pend >= start:
                    stack.append([pst, max(pend, end)])
                else:
                    stack.append(p)
                    stack.append(i)
            else:
                stack.append(i)
                
        return stack