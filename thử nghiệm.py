a = 10
b = 3
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))


'''Một dạng chuỗi mới khác là nội suy chuỗi, f-string. Các chuỗi bắt đầu bằng f và
chúng ta có thể đưa dữ liệu vào các vị trí tương ứng của chúng.(python 3.6)s'''
print(f'{a} + {b} = {a +b}') # 4 + 3 = 7
print(f'{a} - {b} = {a - b}') # 4 - 3 = 1
print(f'{a} * {b} = {a * b}') # 4 * 3 = 12
print(f'{a} / {b} = {a / b:.2f}')# 4 / 3 = 1.33
print(f'{a} % {b} = {a % b}') # 4 % 3 = 1
print(f'{a} // {b} = {a // b}') # 4 // 3 = 1
print(f'{a} ** {b} = {a ** b}') # 4 ** 3 = 64


a = 'Python'
print(a.startswith('Py'))