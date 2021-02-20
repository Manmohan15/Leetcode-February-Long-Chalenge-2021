def romanToInt(self, s1: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=len(s1)-1
        s=0
        s+=d[s1[i]]
        i-=1
        while i>=0:
            # print(i,s)
            if i>=0 and d[s1[i]]<d[s1[i+1]]:
                s-=d[s1[i]]
                i-=1
            elif i>=0 and d[s1[i]]>d[s1[i+1]]:
                s+=d[s1[i]]
                i-=1
            else:
                s+=d[s1[i]]
                i-=1
        return s    
        
