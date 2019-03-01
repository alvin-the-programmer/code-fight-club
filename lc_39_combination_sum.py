class Solution:
    def combinationSumFast(self, candidates, target, memo={}):
        if target <= 0:
            return [[]]
        
        if target in memo: return memo[target]
        
        ways = []
        
        for cand in candidates:
            dif = target - cand
            if dif >= 0:
                ans = self.combinationSumFast(candidates, dif, memo)
                ways += [ [*item, cand] for item in ans]
        
        result_ways = set()
        for way in ways: 
            way.sort()
            result_ways.add(tuple(way))
                
        memo[target] = [list(item) for item in result_ways]
        return memo[target]



    def combinationSumSlow(self, candidates, target):
        print(target)
        if target <= 0:
            return [[]]
                
        ways = []
        
        for cand in candidates:
            dif = target - cand
            if dif >= 0:
                ans = self.combinationSumSlow(candidates, dif)
                ways += [ [*item, cand] for item in ans]
        
        result_ways = set()
        for way in ways: 
            way.sort()
            result_ways.add(tuple(way))
                
        return [list(item) for item in result_ways]

s = Solution()
# print(s.combinationSumFast([1,10,25], 100))
print(s.combinationSumSlow([1,10,25], 100))


