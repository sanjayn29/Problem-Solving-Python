class Solution:
    def primeRange(self, l, r):
        prime = [True]*(r+1)
        prime[0]=prime[1]=False
        for i in range(2,int(r**0.5)+1):
            if prime[i]:
                for j in range(i*i,r+1,i):
                    prime[j]=False
        res=[]
        for i in range(max(2,l),r+1):
            if prime[i]:
                res.append(i)
        return res