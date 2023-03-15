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