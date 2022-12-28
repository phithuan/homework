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
print(a.endswith('on'))


from copy import deepcopy
lst1 = ['a','b',['ab','ba']]
lst2 = deepcopy(lst1)
lst2[2][1] = "d"
lst2[0] = "c"
print ("lst1 = ", lst1)
print ("lst2 = ", lst2)


y = [ [1, 2, 3],[4, 5, 6] ] 
print([row[1] for row in y])
