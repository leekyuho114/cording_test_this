#리스트 slice를 할 때 배열의 복제가 일어나므로 메모리 사용 효율은 좋지 않습니다. (:mid 사용시)
# 1 5 2 4 2 9 7 3 |  1 5 
def merge_sort(array):
    if (len(array) < 2):
        return array
    
    mid = len(array)//2
    low_array = merge_sort(array[:mid])
    high_array = merge_sort(array[mid:])

    merged_array=[]
    l=h=0
    while l<len(low_array) and h<len(high_array):
        if(low_array[l]<high_array[h]):
            merged_array.append(low_array[l])
            l+=1
        else:
            merged_array.append(high_array[h])
            h+=1
    merged_array+=low_array[l:]
    merged_array+=high_array[h:]
    return merged_array

arr=[1,5,2,4,2,9,7,3]

print(merge_sort(arr))
