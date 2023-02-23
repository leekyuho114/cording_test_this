#떡볶이 절단문제, 손님이 요구한 양을 주기위핸 절단기 최댓값
# 설정한 높이마다 조건을 만족했는가를 계속 따지기 떄문에 이진탐색을 떠올려야함

def search_len(array,target,start,end):
    #남은떡길이
    result=0
    while start<=end:
        total=0
        mid=(start+end)//2
        for i in array:
            if(i>=mid):
                total+= (i-mid)
        if total<target:
            end=mid-1
        else:
            result=mid
            start=mid+1
    return result


n,m= map(int, input().split())
array= list(map(int,input().split()))
print(search_len(array,m,0,max(array)))
