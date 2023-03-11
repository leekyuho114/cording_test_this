#이런 식으로 피보나치를 구현하면 지수 시간 복잡도를 가짐
#굉장히 비효율적
# 예를 들어 6번째를 구하기 위해 2번째 피보나치를 5번이나 구하게됨
def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1)+fibo(x-2)

print(fibo(4)) 
