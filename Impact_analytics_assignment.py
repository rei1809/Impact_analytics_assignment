from sys import setrecursionlimit

setrecursionlimit(10**6)

class Graduation:

    def __init__(self,n,m):
        if n < m and n < 0 or m < 0:
            raise Exception("Invalid Inputs")
        
        self.m = m # the number of continuous misses
        self.n = n #the number of days for graduation

    #Recursive
    '''
    TC: exponential 
    SC: O(n * m)
    '''
    def findWays(self):

        def find(ind,m):
            if m == self.m:
                return 0
        
            if ind == 0:
                return 1
            
            return find(ind-1,0) + find(ind-1,m+1)
        
        res1 = find(self.n,0)
        res2 = find(self.n-1,1)

        return f"{res2} / {res1}"

    #using memoisation 
    
    def findWays2(self):
        '''
        TC: O(m*n)
        SC: O(m*n) 
        '''        
        m = self.m
        n = self.n
        dp = [[-1 for i in range(m+1)] for j in range(n+1)]

        def find1(ind,m):
            if m == self.m:
                return 0
        
            if ind == 0:
                return 1
            
            if dp[ind][m] != -1:
                return dp[ind][m]
            
            dp[ind][m] = find1(ind-1,0) + find1(ind-1,m+1)
            return dp[ind][m]
        
        res1 = find1(self.n,0)
        res2 = find1(self.n-1,1)

        return f"{res2} / {res1}"

    #using tabulation 
    def findWays3(self):
        '''
        TC: O(n * m)
        SC: O(n * m)
        '''
        n,m = self.n,self.m

        dp = [[0 for i in range(m+1)]for j in range(n+1)]
        
        for i in range(m):
            dp[0][i] = 1

        for ind in range(1,n+1):
            for miss in range(m-1,-1,-1):
                dp[ind][miss] = dp[ind-1][0] + dp[ind-1][miss+1]

        res1 =  dp[n][0]
        res2 = dp[n-1][1]

        return f"{res2} / {res1}"

    #using tabulation with space optimisation
    def findWays4(self):
        '''
        TC: O(n*m)
        SC: O(m)
        '''
        n, m = self.n, self.m
        dp = [1] * (m + 1)
        dp[m] = 0

        for i in range(1, n + 1):
            prev = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                prev[j] = dp[0] + dp[j + 1]

            prev, dp = dp, prev

        res1 = dp[0]  # total number of valid way to attend classes
        res2 = prev[1]  # total number of way to miss last day

        return f"{res2} / {res1}"

    def run(self):
        print('-' * 40)
        print('n:', self.n, ', misses:', self.m, '\n')
        #print('Using recursion:', self.findWays()) # time limit exceeded for (365,4)
        print('-' * 40)
        print()
        print('Using Memoisation:', self.findWays2()) #TC: O()
        print('-' * 40)
        print()
        print('Using Tabulation method:', self.findWays3())
        print('-' * 40)
        print()
        print('Using Tabulation with space optimisation', self.findWays4())
        print('-' * 40)

if __name__ == "__main__":
    inputs = [(5, 4),(10, 4),(365,4)]
    for n, m in inputs:
        obj = Graduation(n, m)
        obj.run()
