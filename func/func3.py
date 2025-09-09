def info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

# dulri = info(name = '둘리', age = 10)
# douno = info(name = '도우너', age = 8, address = '서울')

def add_text(a, b):
    print(f'{a} {b}')

# add_text('hello', 'world')
# add_text(b='world', a='hello')

def say_text(a):
    if a == '바보':
        return
    print(f'나의 별명은 {a}입니다')

# say_text('짱구')
# say_text('바보')

def cre():
    a = 1
    b = 2
    c = 3
    return a, b, c

# print(cre())

def divide(a, b):
    if b == 0:
        return
    print(a // b)

# divide(10, 2)
# divide(10, 0)

def add(a, b):
    if type(a) != int or type(b) != int:
        print('입력받은 값이 숫자가 아닙니다')
        return
    else:
        print(f'{a} + {b} = {a + b}')

# add(12, 14)
# add(3, 4)
# add(3, 'ss')

