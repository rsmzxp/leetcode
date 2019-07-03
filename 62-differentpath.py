import numpy as np
class Solution(object):
    #通过分析计算组合数
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.my_combination(m+n-2,m-1)
    def my_step_multi(self,n):
        """
        n计算n的阶乘
        """
        result=1
        for i in range(1,n+1):
          result *= i
        return result

    def my_combination(self,m,n):
        '''
        m,n表示从m个样品中抽取n个
        '''
        if m<n:
            return False
        return self.my_step_multi(m)/(self.my_step_multi(n)*self.my_step_multi(m-n))
    
    def uniquePaths2(self, m, n):
        #通过动态规划记录路径的方式
         dp = np.array([1 for _ in range(m*n)]).reshape(m,n)
         for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
         return dp[m-1][n-1]
