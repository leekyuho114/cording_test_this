array = [7,5,9,0,3,1,6,2,4,8]

#선택 정렬
for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if(array[j]<=array[min_index]):
            min_index=j
    array[i], array[min_index] = array[min_index], array[i] 
#값 바꿔주는거 c에서는 temp 로 바꿔줘야됨

#삽입 정렬
for i in range(1, len(array)):
    for j in range(i,0,-1):
        if(array[j] < array[j-1]):
            temp=array[j]
            array[j]=array[j-1]
            array[j-1]=temp
        else:
            break
print(array)

#퀵 정렬 - 표준적으로 사용
