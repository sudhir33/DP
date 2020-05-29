w=[2,4,6,5]
v=[2,3,1,4]
c=8
sol=[]
dp=[[0 for i in range(c+1)] for j in range(len(w)+1)]
"""
for i in range(len(v)+1):
    for j in range(c+1):
        print(dp[i][j],end=" ")
    print()
"""
for i in range(len(w)+1):
    for j in range(c+1):
        if i==0 and j==0:
            continue
        if w[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            v1=v[i-1]+dp[i-1][j-w[i-1]]
            v2=dp[i-1][j]
            dp[i][j]=max(v1,v2)
            
print(dp[-1][-1])
#print(sol)




            
            
            
