#계수정렬
#최악의 경우에도 O(n+k) 보장
#정수인 경우만 가능
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

#count = [0]*(max(array)+1) 이걸로 대체 가능
temp=0
for i in array:
    if(i>temp):
        temp=i

count =[0]*(temp+1)

for i in range(len(array)):
    count[array[i]]+=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')