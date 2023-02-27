#두 리스트 먼저 정렬 앞에서부터 뒤에서부터 대충 더해서 출력

n, k = map(int, input().split())

arrayA=list(map(int, input().split()))
arrayB=list(map(int, input().split()))

arrayA.sort(reverse=True)
arrayB.sort(reverse=True)
result=0
#arrayB 큰거부터 k개 바꿔치기
for i in range(k):
    result+=(arrayB[i])
#arrayA 큰거부터 n-k개 더하기
for i in range(n-k):
    result+=(arrayA[i])
print(k,n-k)
print(arrayA,arrayB, result)
