#최대 공약수 유클리드 호제법
def GCD(a, b):
    # 나머지가 0일시 종료
    if a%b ==0:
        return b;
    else:
        return GCD(b, a%b);

print(GCD(192,162));
