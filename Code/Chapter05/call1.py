def f(x):
    y = x
    x = 5   # 이것도 call2.py에서 함수의 호출 방식과 비슷한 원리
    return y*y

x = 3
print(f(x))
print(x)
