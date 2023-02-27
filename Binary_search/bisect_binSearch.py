#bisect_left(array,x)는 array에 x가 들어갈 가장 왼쪽원소
#bisect_right(array,x)는 array에 x가 들어갈 가장 오른쪽원소

from bisect import bisect_left,  bisect_right

array=[1,2,4,4,8]
x=4
print(bisect_left(array, x))
print(bisect_right(array, x))

#이 bisect를 통해 값이 특정범위에 속하는 데이터 개수 구하기

def count_by_range(array,left_value,right_value):
    right_index=bisect_right(array,right_value)
    left_index=bisect_left(array,left_value)
    return right_index-left_index

array= [1,2,3,3,3,3,4,4,8,9]
#값이 4인  데이터 개수 출력
print(count_by_range(array,4,4))
#값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(array,-1,3))
