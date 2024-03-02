#các bài tập về HÀN 
#giá trị tuyệt đối
n=int(input('nhập một số bất kì: '))
def gttt(n):
    if n>=0 :
        return n
    else :
        return -n

print('giá trị tuyệt đối của ',n,'là',gttt(n))

--------------------------------------------------------------------------------------------------------------------------------------------------------
def chao(ten):
    print('chào bạn nhé '+ten)

a=input('nhập họ tên: ')
chao(a)

-------------------------------------------------------------------------------------------------------------------------------------------------------
#ĐỆ UY
i=1
def lap(i):
    print('điền vào đê nhóc hết kìa: ')
    if i < 5 :
        lap(i+1)

lap(i)

----------------------------------------------------------------------------------------------------------------------------------------------------------
#tìm ước chung lớn nhất với cú pháp hàm\

a=int(input('nhập a: '))
b=int(input('nhập b: '))

def ucll(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
print('ước chung lớn nhất của %d và %d là: %d'%(a,b,ucll(a,b)))

---------------------------------------------
a=int(input('nhập một số bát kì để tìm giai thừa: '))
def gt(a):
    if a==0:
        return 1
    else:
        return a*gt(a-1)

print('gia thừa của %d là: '%(a),gt(a))

-----------------------------------------------------
a=int(input('nhập số a'))
b=int(input('nhập số b'))
c=int(input('nhập số c'))


def min(a,b):
    if a<b:
        return a
    else:
        return  b

print('số nhỏ nhất trong ba số %d %d %d là: '%(a,b,c),min(min (a,b),c))
------------------------------------------------------------------------
#mãng nhiều chiều 
#bài tính tổng
a=[[12,5,7,3],[2,8,4,2]]
row=len(a)
tong=0
for i in range(row):
    col=len(a[i])
    for j in range(col):
        tong=tong+a[i][j]

print('tổng là ',tong)


#tìm số lớn nhất
a=[[12,5,7,3],[2,8,4,2]]
row=len(a)
max=a[0][0]
for i in range(row):
    col=len(a[i])
    for j in range(col):
        if a[i][j]>max:
            max=a[i][j]

print(a)
print('số lớn nhất',max)


#đảo 
a=[[12,5,7,3],[2,8,4,2]]
b=a[::-1]
for i in range(len(b)):
    c=b[i][::-1]
    print(c,end='')

-------------------------------------------------------------------------
"""nums_list = [2,7,11,15]
target = 9
lst= []
for i in range(len(nums_list)):
    for j in range(len(nums_list)):
        a= nums_list[0] + nums_list[j]
        if a==target:
            print(nums_list.index(nums_list[j]))"""

"""nums=[]
print('Nhập vào số phần tử của dãy')
so_phan_tu=int(input())
print('Nhập vào số nguyên')
So_nguyen=int(input())
print('Nhập vào lan lượt giá trị các phần tử')
for i in range (0,so_phan_tu):
    Gia_tri=int(input())
    nums.append(Gia_tri)
for i in range(0,len(nums)-1):
    for k in range(i+1,len(nums)):
        if int(nums[i])+int(nums[k])==So_nguyen:  
            print(i,k)
            k=len(nums)                   
print(len(nums))"""        