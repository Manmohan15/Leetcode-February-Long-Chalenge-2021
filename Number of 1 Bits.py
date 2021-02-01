class Solution:
    def hammingWeight(self, n: int) -> int:
        b=bin(n);
        count=0;
        for i in range(2,len(b)):
            if(b[i]=='1'):
                count+=1
        return count        
        
    def hammingWeight(self, n: int) -> int:
        count=0
        mask=1
        for i in range(0,32):
            if(n & mask):
                count+=1
            mask<<=1
        return count    
        
     def hammingWeight(self, n: int) -> int:
        count=0
        while(n!=0):
            count+=1
            n&=(n-1)
        return count        
            
