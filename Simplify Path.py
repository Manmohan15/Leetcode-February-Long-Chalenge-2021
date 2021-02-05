class Solution:
    def simplifyPath(self, path: str) -> str:
        l=list(re.split('/|//',path))
        stack=[]
        for i in l:
            if i=='.':
                continue
            elif i=='..':
                if len(stack)!=0:
                    stack.pop(-1)
            elif i!="":
                stack.append(i)
        s=""        
        for j in range(0,len(stack)):
            s+='/'
            s+=stack[j]
        if len(stack)==0:
            return '/'
        return s    
            
                
                
        
