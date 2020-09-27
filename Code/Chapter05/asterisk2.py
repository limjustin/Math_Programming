def asterisk_test(a,b,*args):
    print(args)     # 얘가 먼저 출력

print(asterisk_test(1,2,3,4,5))     # 그 다음에 출력
