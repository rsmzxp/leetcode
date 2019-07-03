class Solution(object):
    #
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
