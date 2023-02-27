array = [5,7,9,0,3,1,6,2,4,8]

def quickSort(array, start, end):
    if (start>=end):
        return
    pivot = start
    left = start +1
    right= end
    while(left<=right):
        while(left<=end and array[left] <= array[pivot]):
            left+=1
        #여기 right>=start로 가면 pivot과 비교하기때문에 코드 안돌아가게됨
        while(right>start and array[right] >= array[pivot]):
            right-=1
        if(left>right):
            temp=array[pivot]
            array[pivot]= array[right]
            array[right]=temp
        else:
            temp=array[left]
            array[left]= array[right]
            array[right]=temp

    quickSort(array, start, right-1)
    quickSort(array, right+1, end)


quickSort(array, 0, len(array)-1)
print(array)
