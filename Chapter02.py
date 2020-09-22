## Chapter 02. 변수와 자료형

# 1. 변수의 이해
professor = "Sungchul Choi"
print(professor)

a = 7
b = 5
print(a+b)

a = 7
b = 5
print("a+b")

# 2. 자료형과 기본 연산
a = 1
b = 1
print(a,b)

a = 1.5
b = 3.5
print(a,b)

a = "ABC"
b = "101010"
print(a,b)

a = True
b = False
print(a,b)

print(25+30)
print(30-12)
print(50*3)
print(30/5)

print(3*3*3*3*3)
print(3**5)

print(7 // 2)
print(7 % 2)

a = 1
a = a + 1
print(a)

a += 1
print(a)

a = a - 1
a -= 1
print(a)

# 3. 자료형 변환
a = 10
print(a)

a = float(10)
print(a)

a = 10
b = 3
print(a/b)

a = int(10.7)
b = int(10.3)

print(a+b)
print(a)
print(b)

a = '76.3'
b = float(a)
print(a)
print(b)
# print(a+b) # 문자열과 숫자열의 덧셈 불가능

a = float(a)
b = a
print(a + b)

a = str(a)
b = str(b)
print(a+b)

a = int(10.3)
b = float(10.3)
c = str(10.3)

print(type(a))
print(type(b))
print(type(c))