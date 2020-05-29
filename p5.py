"""
minimum subset sum difference
0-1 knapsack
29-may-2020
"""
arr=[1,5,11,5]#[1,2,7]#[1,2,3,5,13]
s=sum(arr)
sub=s//2
n=len(arr)#size of array
"""
create a double array with length of array as rows and s columns in each row
"""
dp=[[False for i in range(sub+1)] for j in range(n+1)]
for i in range(n+1):
    dp[i][0]=True
"""
for i in range(n+1):
    for j in range(s+1):
        print(dp[i][j],end=" ")
    print()
"""
for i in range(1,n+1):
    for j in range(1,sub+1):
        if arr[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            if dp[i-1][j]==True:
                val=True
            else:
                val=dp[i-1][j-arr[i-1]]
            dp[i][j]=val

res=dp[-1]

for i in range(len(res)-1,-1,-1):
    if res[i]==True:
        fp=i
        break
    
sp=s-fp
print(abs(fp-sp))
    
            

    

