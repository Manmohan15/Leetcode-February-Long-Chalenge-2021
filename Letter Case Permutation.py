def letterCasePermutation(self, S: str) -> List[str]:
        def solve(l,s,i):
            # print("l",l)
            if i==len(s):
                return l
            if(len(l)==0):
                l.add(s[i].upper())
                l.add(s[i].lower())
            else:
                c=set()
                d=set()
                for j in l:
                    c.add(j+s[i].upper())
                    d.add(j+s[i].lower())
                l=c.union(d)
            l=solve(l,s,i+1)  
            return l
        l=set()
        set1=solve(l,S,0)
        l1=[i for i in set1]
        return l1
                    
