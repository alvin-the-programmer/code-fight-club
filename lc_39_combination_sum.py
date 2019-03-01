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
        
        uniqs = set([ tuple(sorted(l)) for l in ways ])
        memo[target] = [ list(t) for t in uniqs ]
        return memo[target]

    def combinationSumSlow(self, candidates, target):
        if target <= 0:
            return [[]]
                
        ways = []
        
        for cand in candidates:
            dif = target - cand
            if dif >= 0:
                ans = self.combinationSumSlow(candidates, dif)
                ways += [ [*item, cand] for item in ans]
        
        uniqs = set([ tuple(sorted(l)) for l in ways ])
        return [ list(t) for t in uniqs ]

s = Solution()
print(s.combinationSumFast([1,10,25], 100))
# print(s.combinationSumSlow([1,10,25], 100))


