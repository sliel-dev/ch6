def calc(**kawargs):
    for key in kawargs.keys():
        print(key)

# calc(apple=1200, banana=800, orange=1500)

def show_scores(**kawargs):
    for val in kawargs.values():
        print(val)

# show_scores(철수=90, 영희=85, 민수=100)

def show_pop(**kawargs):
    for key, val in kawargs.items():
        print(key, val)

# show_pop(seoul=950, busan=340, incheon=300)

def show_item(**kawargs):
    for key in kawargs.keys():
        print(key)        

# show_item(milk=2500, bread=2000, egg=3000)

def sub(a, b):
    return a - b

# result = sub(10, 12)
# print(result)

# result = sub(b=10, a=12)
# print(result)

def age(a):
    if type(a) != int or a < 0 :
        print('잘못된 입력입니다')
        return
    if a >= 20:
        print('성인입니다')
    else:
        print('성인이 아닙니다')

# age(-1)

def info(name, age, gender='m'):
    print(f'나의 이름은 {name} {age}살이야')
    if gender == 'm':
        print('남자지')
    else:
        print('여자지')

info('둘리', 10)
info('도우너', 8, 'f')