"""
subset problem    True/False
0-1knapsack problem
29-may-2020
"""
arr=[2,3,7,8,10]
s=11#sum
n=len(arr)#size of array
"""
create a double array with length of array as rows and s columns in each row
"""
dp=[[False for i in range(s+1)] for j in range(n+1)]
for i in range(n+1):
    dp[i][0]=True
"""
for i in range(n+1):
    for j in range(s+1):
        print(dp[i][j],end=" ")
    print()
"""
for i in range(1,n+1):
    for j in range(1,s+1):
        if arr[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            if dp[i-1][j]==True:
                val=True
            else:
                val=dp[i-1][j-arr[i-1]]
            dp[i][j]=val
for i in range(n+1):
    for j in range(s+1):
        print(dp[i][j],end=" ")
    print()                
            



















