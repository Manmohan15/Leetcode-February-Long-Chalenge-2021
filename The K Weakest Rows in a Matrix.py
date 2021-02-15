class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l=[]
        for i in range(len(mat)):
            l.append([i,mat[i].count(1)])
        l.sort(key=lambda x:x[1]*1000000+x[0])
        ans=[]
        for i in range(0,k):
            ans.append(l[i][0])
        return ans
        
