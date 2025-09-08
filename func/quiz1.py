# nick_name = input()
# def name():
#     return '님, 환영합니다!'
# print(nick_name, name())

# def hi(name, msg):
#     print(f'{name}님,{msg}')
# hi(input(), input())

# def sum(a, b):
#     num = 0
#     for n in range(a, b + 1):
#         num = num + n
#     print(num)
# sum(5, 10)

# def minus(a, b):
#     if a < b:
#         return -999
#     else:
#         return a - b

# print(minus(20, 10))

# def holjak(a):
#     if a % 2 == 0:
#         return '짝수'
#     else:
#         return '홀수'

# print(holjak(10))

# def st(a):
#     if type(a) == str:
#         print('문자입니다')

# st('qwer')
# 양수/음수/0 판별 함수
# def num(a):
#     if a > 0:
#         print('양수입니다')
#     elif a == 0:
#         print('0입니다')
#     else:
#         print('음수입니다')
    
# num(1)

# def lis(a):
#     if type(a) == list:
#         return a[0]

# asd = [10, 20, 30, 40]
# sdd = ['a', 'b', 'c']
# qwe = 123123
# wewe = 'str'
# print(lis(asd), lis(sdd), lis(qwe), lis(wewe))

# def lens(a):
#     a = len(a)
#     print(a)

# lens('qwertyuiop')

# def lis(a):
#     sum = 0
#     for n in range(len(a)):
#         sum = sum + int(a[n])
#     print(sum)

# asd = [10, 20, 30, 40]
# wq = [1, 2, 3, 4, 5]
# lis(wq)

# def gop(a):
#     for n in range(1, 10):
#         gopsem = 0
#         gopsem = a * n
#         print(gopsem)

# gop(3)

def str_cnt(a):
    cnt = 0
    for n in range(len(a)):
        if type(a[n]) == str:
            cnt+=1
    print(cnt)


ssa = [1, 'apple', 2, 'banana', 10, 'hi']
str_cnt(ssa)