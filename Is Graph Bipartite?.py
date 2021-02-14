class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(graph,q,color,src):
            color[src]=1
            q.append(src)
            while(len(q)!=0):
                p=q.pop()
                for i in graph[p]:
                    if(color[i]==color[p]):
                        return False
                    elif(color[i]==-1):
                        color[i]=1-color[p]
                        q.append(i)
                    elif(i==p):
                        return False
            return True            
        n=len(graph)   
        color=[-1]*n
        q=[]
        for i in range(0,len(color)):
            if(color[i]==-1):
                if(dfs(graph,q,color,i)==False):
                    return False
        return True     
