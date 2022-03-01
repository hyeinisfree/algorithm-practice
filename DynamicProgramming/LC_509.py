# naive fibonacci
def fib_naive(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_naive(n-1)+fib_naive(n-2)

#Recursive Dynamic Programming
#Top Down
fib_arry = [0,1]
def fib_recur_dp(n):    
    cnrt_length = len(fib_arry)
    if n<cnrt_length:
        return fib_arry[n] 
    else:
        fib = fib_recur_dp(n-1)+fib_recur_dp(n-2)
        fib_arry.append(fib)
        return fib
    
#Bottom Up Fibonacci Approach
def fib_dp(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    fib_array = [0,1]  
    for i in range(2,n+1):        
        num = fib_array[i-1]+fib_array[i-2]
        fib_array.append(num)
    return fib_array[n]