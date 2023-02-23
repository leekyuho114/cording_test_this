# 먼저 sort 된 상태에서 반씩 잘라나가며 탐색
#어떠한 값이 존재하는지 유무를 확인할때 사용
#재귀함수를 통해 구현
def binary_search_recursive(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] ==target:
        return mid
    elif array[mid] >target:
        return binary_search_recursive(array, target, start,mid-1)
    else:
        return binary_search_recursive(array, target, mid+1 ,end)

#반복문을 통해 구현
def binary_search_loop(array,target,start,end):
    while start<= end:
        mid = (start+end)//2
        if array[mid]== target:
            return mid
        elif array[mid] > target:
            end= mid-1
        else:
            start=mid+1
    return None

n, target = map(int, input().split())
array = list(map(int,input().split()))
result=binary_search_loop(array,target,0,n-1)
if(result==None):
    print("None")
else:
    print(result+1)