"""
equal sum partition problem   o/p: True or False
0-1 knapsack problem
29-may-2020
"""
arr=[1,5,11,5]# good input[1,5,11,9]
s=sum(arr)
if s%2==0:
    s=s//2
    n=len(arr)#size of array

    dp=[[False for i in range(s+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True

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
                
else:
    print(False)
