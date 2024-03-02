def MergeTwoSortedLists():    
    firstList = [2, 7, 8, 9]
    secondList = [1, 1, 4, 6]
    arr = firstList + secondList
    print(arr)

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    for num in arr:
        print(num, end=" ")



def twosum():
    nums_list = [2,7,11,15]
    target = 9
    for i in range(len(nums_list)):
        for j in range(i+1,len(nums_list)):
            if nums_list[i] + nums_list[j]==target:
                print(i,j)

def vd1():
    class hcn():
        def __init__(self,cd,cr):
            self.cd=cd
            self.cr=cr

        def show(self):
            print('chiều dài hình chữ nhật là: ',self.cd)
            print('chiều rộng hình chữ nhật là: ',self.cr)

        def dientich(self):
            return (self.cd * self.cr)

        def chuvi(self):
            return(self.cd + self.cr)*2

    hcn1=hcn(4,5)

    hcn1.show()
    print('diện tích và chu vi hình chữ nhật lần lượt là: ',hcn1.dientich(), hcn1.chuvi())



def removeElement():
    nums = input("Nhập vào danh sách các số, cách nhau bằng khoảng trắng: ").split()
    nums = [int(x) for x in nums]
    val = int(input("Nhập vào giá trị cần xóa: "))

    insert_idx = 0
    for i in range(len(nums)):
        print("Vòng lặp thứ", i+1)
        print("Giá trị hiện tại của nums:", nums)
        if nums[i] != val:
            nums[insert_idx] = nums[i]
            insert_idx += 1
        else:
            nums[insert_idx] = "-"
            print("Giá trị mới của nums:", nums)
            print("Vị trí con trỏ chèn phần tử mới:", insert_idx)
    new_nums = nums[:insert_idx]
    print("Danh sách mới sau khi xóa các phần tử có giá trị bằng", val, "là:", new_nums)
    print("Độ dài mới của danh sách là:", len(new_nums))
    return len(new_nums), new_nums

def removeElement1():
    nums = input("Nhập vào danh sách các số, cách nhau bằng khoảng trắng: ").split()
    nums = [int(x) for x in nums]
    val = int(input("Nhập vào giá trị cần xóa: "))
    
    new_nums = []
    for num in nums:
        if num != val:
            new_nums.append(num)
    
    print("Danh sách mới sau khi xóa các phần tử có giá trị bằng", val, "là:", new_nums)
    print("Độ dài mới của danh sách là:", len(new_nums))
    return len(new_nums), new_nums

"""def addDigits(num):
    while num >= 10:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        num = digit_sum
    return num

num = int(input("Nhập vào số nguyên dương: "))
digit_sum = addDigits(num)
print("Tổng chữ số của", num, "là:", digit_sum)"""



def CS():
    candidates = [2,3,6,7,5]
    target = 7
    for i in range(len(candidates)):
        if candidates[i] == target:
            print(candidates[i], "is a candidate")
        if candidates[i] < target:
            for j in range (len(candidates)-1):
                #print(candidates[i],[j])
                #print(candidates[j])
                if candidates[i] + candidates[j]==target:
                    i=+i
                    print(candidates[i],candidates[j])
                if candidates[0] + candidates[0] + candidates[1] == target:
                    print(candidates[0] , candidates[0] , candidates[1])
CS()