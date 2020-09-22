## Chapter 04. 조건문과 반복문

# 1. 조건문
print("Tell me your age?")
myage = int(input())
if myage < 30:
    print("Welcome to the Club.")
else:
    print("Oh! No. You are not accepted.")

print(7 == 7)

a = 100
b = 100
print(a is b)
print(a == b)
a = 300
b = 300
print(a == b)
print(a is b)

print((3>5) < 10)

a = 8
b = 5
print(a == 8 and b == 4)
print(a>7 or b>7)
print(not(a>7))

score = int(input("Enter your score: "))

if score >= 90:
    grade = 'A'
if score >= 80:
    grade = 'B'
if score >= 70:
    grade = 'C'
if score >= 60:
    grade = 'D'
if score < 60:
    grade = 'F'

print(grade)

score = int(input("Enter your score: "))

if score >= 90: grade = 'A'
elif score >= 80: grade = 'B'
elif score >= 70: grade = 'C'
elif score >= 60: grade = 'D'
else: grade = 'F'

print(grade)

# 2. Lab: 어떤 종류의 학생인지 맞히기
print("당신이 태어난 연도를 입력하세요.")
birth_year = input()
age = 2020 - int(birth_year) + 1

if age <= 26 and age >= 20:
    print("대학생")
elif age < 20 and age >= 17:
    print("고등학생")
elif age < 17 and age >= 14:
    print("중학생")
elif age < 14 and age >= 8:
    print("초등학생")
else:
    print("학생이 아닙니다.")

print(1<=2<10)
print(1<=100<10)

# 3. 반복문
for looper in [1,2,3,4,5]:
    print("hello")

for looper in [1,2,3,4,5]:
    print(looper)

for looper in range(100):
    print("hello")

for i in 'abcdefg':
    print(i)

for i in ['americano', 'latte', 'frappuccino']:
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(10,1,-1):
    print(i)

i = 1
while i < 10:
    print(i)
    i += 1

for i in range(10):
    if i == 5: break
    print(i)
print("End of Program")

for i in range(10):
    if i == 5: continue
    print(i)
print("End of Program")

for i in range(10):
    print(i)
else:
    print("End of Program")

# 4. Lab: 구구단 계산기
print("구구단 몇 단을 계산할까?")
user_input = input()
print("구구단", user_input, "단을 계산한다.")
int_input = int(user_input)
for i in range(1, 10):
    result = int_input + i
    print(user_input, "x", i, "=", result)

# 5. 조건문과 반복문 실습
sentence = "I love you"
reverse_sentence = ''
for char in sentence:
    reverse_sentence = char + reverse_sentence
print(reverse_sentence)

decimal = 10
result = ''
while(decimal > 0):
    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result
print(result)

# 6. Lab: 숫자 찾기 게임
import random
guess_number = random.randint(1, 100)
print("숫자를 맞혀 보세요. (1~100)")
users_input = int(input())
while(users_input is not guess_number):
    if users_input > guess_number:
        print("숫자가 너무 큽니다.")
    else:
        print("숫자가 너무 작습니다.")
    users_input = int(input())
else:
    print("정답입니다.", "입력한 숫자는", users_input, "입니다.")

# 7. Lab: 연속적인 구구단 계산기
print("구구단 몇 단을 계산할까요(1~9)?")
x = 1
while(x is not 0):
    x = int(input())
    if x == 0: break
    if not(1<= x <= 9):
        print("잘못 입력했습니다", "1부터 9 사이 숫자를 입력하세요.")
        continue
    else:
        print("구구단" + str(x) + "단을 계산합니다.")
        for i in range(1, 10):
            print(str(x) + "x" + str(i) + "=" + str(x*i))
        print("구구단 몇 단을 계산할까요(1~9)?")
print("구구단 게임을 종료합니다.")

# 8. Lab: 평균 구하기
kor_score = [49,80,20,100,80]
math_score = [43,60,85,30,90]
eng_score = [49,82,48,50,100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0,0,0,0,0]
i = 0
for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0
else :
    a,b,c,d,e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print(student_average)

# 9. 코드의 오류를 처리하는 방법
x = 2
 # y = 5
print(x+y)

# pront(x+y)
korean = "ACE"
# print(Korean)

def addition(x,y):
    return x + y

def multiplication(x,y):
    return x * y

def divided_by_2(x):
    return x / 2

# import trapezium_def as ta
# print(ta.addition(10,5))
# print(ta.multiplication(10,5))
# print(ta.divided_by_2(50))

def addition(x,y):
    return x + y

def multiplication(x,y):
    return x * y

def divided_by_2(x):
    return x / 2

if __name__ == '__main__':
    print(addition(10,5))
    print(multiplication(10,5))
    print(divided_by_2(50))

def addition(x,y):
    return x + y

def divided_by_2(x):
    return x / 2

def main():
    base_line = float(input("밑변의 길이는? "))
    upper_edge = float(input("윗변의 길이는? "))
    height = float(input("높이는? "))

    print("넓이는:", divided_by_2(addition((base_line, upper_edge) * height)))

if __name__ == '__main__':
    main()