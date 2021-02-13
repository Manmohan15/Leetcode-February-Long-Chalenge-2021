class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        vector<vector<bool>>visited(grid.size(),vector<bool>(grid.size(),false));
        queue<pair<int,int>>q;
        q.push(make_pair(0,0));
        visited[0][0]=true;
        int c=0;
        int n=grid.size();
        if(grid[0][0]==1 or grid[n-1][n-1]==1){
            return -1;
        }
            
            while(!q.empty())
            {
                c+=1;
//                 for(int i=0;i<q.size();i++)
//                 {
//                     cout<<q[i].first<<q[i].second<<c<<endl;
//                 }
                int si=q.size();
                for(int i=0;i<si;i++)
                {   
                    pair<int,int>curr=q.front();
                    int x=curr.first;
                    int y=curr.second;
                    q.pop();
                    if(x==n-1 && y==n-1)
                    {
                    // {   cout<<"fnid"<<c;
                        return c;
                    }
        
                    for(int j=-1;j<=1;j++)
                    {
                        for(int k=-1;k<=1;k++)
                        {
                            if(x+j>=0 && x+j<n && y+k>=0 && y+k<n && !visited[x+j][y+k] && grid[x+j][y+k]!=1)
                            {
                            // {   cout<<x+j<<y+k<<c<<endl;
                                q.push(make_pair(x+j,y+k));
                                visited[x+j][y+k]=true;
                    
                                }
                            }
                            
                        }
                    }
                    
                }
            
        return -1;
        
    }
};
