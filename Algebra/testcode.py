''' 执行一代码测试 '''
p = [9, 5, 3]
print(p * 3)

print('{:^14}'.format('陈某某'))
print('{:>14}'.format('陈某某'))
print('{:<14}'.format('陈某某'))
print('{:*<14}'.format('陈某某'))  # 用14个字符的宽度，左对齐，其他字符用*填充
print('{:&>14}'.format('陈某某'))  # 填充和对齐^<>分别表示居中、左对齐、右对齐，后面带宽度
for i in range(5, -1, -1):
    print(i)



p = 2
if not p:
    print("p none")