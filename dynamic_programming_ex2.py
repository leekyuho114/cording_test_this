#피보나치 처럼 여러 문제가 중복됨 -> 트리로 표현 == 최적부분구조
#그리고 그 문제들이 여러번 중복됨 == 중복되는 부분문제
n = int(input())

d = [0]*30001
#range의 경우 start end 모두 작성시 뒤에 +1까지 해줘야함
for i in range(2,n+1):
    # 1을 빼는 경우
    d[i] = d[i-1]+1
    if i % 2 == 0:
        d[i]=min(d[i],d[i//2]+1)
    if i % 3 == 0:
        d[i]=min(d[i],d[i//3]+1)
    if i % 5 == 0:
        d[i]=min(d[i],d[i//5]+1)
print(d[n])
