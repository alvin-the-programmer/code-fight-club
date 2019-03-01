
# say the 0th is 0, 1st is 1
# 1,1,2,3,5,8,13

# def fib(n):
#     if n < 2: return n
#     return fib(n - 1) + fib(n - 2) 

# 1 - write the brute force code
# 2 - add the memo obj as another arg
# 3 - at the top, add a base case, if the input is in the memo, then return it
# 4 - when we make a recursive call, save the result in the memo

def fib_memo(n, memo={0:0, 1:1}):
    if n in memo: return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo) 
    return memo[n]

# print(fib(5)) #=> 5
# print(fib(6)) #=> 8
# print(fib(9)) #=> 34
print(fib_memo(10)) #=> 55



