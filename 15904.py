import sys
input = sys.stdin.readline
words = input()

target = ['U', 'C', 'P', 'C']

upper = ''
for char in words:
    if char.isupper() == True:
        upper += char

idx = 0
result = ''
for A in upper:
  if result == 'UCPC':
    break
  elif A == target[idx]:
    result += A
    idx += 1

if result == 'UCPC':
    print('I love UCPC')
else:
    print('I hate UCPC')