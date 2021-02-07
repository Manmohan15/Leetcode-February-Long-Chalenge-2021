class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        f=set()
        for i in range(0,len(s)):
            if(s[i]==c):
                f.add(i)       
        res=[]        
        for i in range(0,len(s)):
            min1=float('inf')
            for j in f:
                min1=min(min1,abs(i-j))
            res.append(min1)
        return res    
                
