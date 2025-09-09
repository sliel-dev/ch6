f = open('test.txt', 'w')
a = 'hello'
b = 'hi'
f.write(f'{a}\n{b}')
f.close()

f = open('score.txt', 'w')
f.write('80 90 70 100 60')
f.close()

f = open('numbers.txt', 'w')
for n in range(10, 21):
    f.write(f'{n}\n')
f.close()