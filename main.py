def recursive_function(i):
    #100번째 호출을 했을 시 종료 (종료조건 꼭 명시)
    if i ==100:
        return
    print(i ,'번째 재귀함수에서 ',i+1,"번째 재귀함수 호출")
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료')


recursive_function(1)
#파이썬은 재귀 깊이 제한 있어서 멈춤