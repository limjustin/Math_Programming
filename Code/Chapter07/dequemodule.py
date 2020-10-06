from collections import deque
deque_list = deque()
for i in range(5):
    deque_list.appendleft(i)

print(deque_list)
print(deque_list.rotate(2))
print(deque_list)
print(deque_list.rotate(2))
print(deque_list)
