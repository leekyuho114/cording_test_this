n= int(input())
array = list(map(int, input().split()))
# a(i) = i번째 식량창고 까지의 최적의 해(최댓값)
# 1 3 1 5 
# a(0)=1 a(1)=3 a(2)=3 a(3)=8
# a(n)에 올 수 있는 경우는 2가지임
# a(i) = max( a(i-1), a(i-2)+k(i) )
d=[0] * 100
d[0] = array[0]
d[1] = max(array[0],array[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[3])