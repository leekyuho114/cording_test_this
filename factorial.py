#반복으로 구현한 n!
def factorial_iterative(n):
    result=1
    for i in range(1,n+1):
        result *= i
    return result

def factorial_recursive(n): #1일 경우 return 1 아닐경우 함수 *n
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)

print("iterative: ", factorial_iterative(5))
print("iterative: ", factorial_recursive(5))