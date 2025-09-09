# f = open('새파일.txt', 'w')

# f.write('a b c d e')

# f.close()

# f = open('file1.txt', 'w')

# for n in range(1, 11):
#     f.write(str(n))

# f.close()
f = open('file2.txt', 'w', encoding='utf-8')
for i in range(1, 11):
    f.write(f'{i}번째 줄\n')

f.close()