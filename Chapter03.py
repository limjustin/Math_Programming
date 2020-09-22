## Chapter 03. 화면 입출력과 리스트

# 2. 화면 입출력
print("Enter your name:")
somebody = input()
print("Hi", somebody, "How are you today?")

print("Hello World!", "Hello Again!!!")

temperature = float(input("온도를 입력하세요: "))
print(temperature)

# 3. Lab: 화씨온도 변환기
print("본 프로그램은 섭씨온도를 화씨온도로 변환하는 프로그램입니다.")
print("변환하고 싶은 섭씨온도를 입력하세요.")

celsius = input()
fahrenheit = (float(celsius) * 1.8) + 32

print("섭씨온도:", celsius)
print("화씨온도:", fahrenheit)

# 4. 리스트의 이해
colors = ['red', 'blue', 'green']
print(colors[0])
print(colors[2])
print(len(colors))

cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
print(cities[0:6])
print(cities[0:5])
print(cities[5:])

print(cities[-8:])

print(cities[:])
print(cities[-50:50])

print(cities[::2])
print(cities[::-1])

color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white']
print(color1 + color2)
print(len(color1))
total_color = color1 + color2
print(total_color)

print(color1 * 2)
print('blue' in color2)

color = ['red', 'blue', 'green']
color.append('white')
print(color)

color.extend(['black', 'purple'])
print(color)

color = ['red', 'blue', 'green']
color.insert(0, 'orange')
print(color)

print(color)
color.remove('red')
print(color)

color = ['red', 'blue', 'green']
color[0] = 'orange'
print(color)
del color[0]
print(color)

t = [1,2,3]
a, b, c = t
print(t, a, b, c)

# a,b,c,d,e = t  # not enough values to unpack
# a,b = t  # too many values to unpack

kor_score = [49,79,20,100,80]
math_score = [43,59,85,30,90]
eng_score = [49,79,48,60,100]
midterm_score = [kor_score, math_score, eng_score]
print(midterm_score)

print(midterm_score[0][2])

# 5. 리스트의 메모리 관리 방식
kor_score = [49,79,20,100,80]
math_score = [43,59,85,30,90]
eng_score = [49,79,48,60,100]
midterm_score = [kor_score, math_score, eng_score]
print(midterm_score)
math_score[0] = 1000
print(midterm_score)

a = 300
b = 300
print(a is b)
print(a == b)

a = 1
b = 1
print(a is b)
print(a == b)

a = ["color", 1, 0.2]
color = ['yellow', 'blue', 'green', 'black', 'purple']
a[0] = color
print(a)

a = [5,4,3,2,1]
b = [1,2,3,4,5]
b = a
print(b)

a.sort()
print(b)

b = [6,7,8,9,10]
print(a,b)