#bai1
def tinhhetcaroi():
    dt= float(input("DOANH THU:"))
    cp= float(input("CHI PHI:"))
    roi = (dt - cp)/cp
    print("chỉ số ROI của bạn",roi)
    if roi >= 0.75:
        print("Đầu tư đi thg lz")
    else:
        print("Đầu tư là cháy tài khoản đó thg ngu này")

#bai2
def fibonacci(n):
    if n ==1 or n==0:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#print("những số đầu tiên của dãy số fibonacci:")
fib = ""
for i in range(1,12):
    fib += str(fibonacci(i)) + ","
#print(fib,"...")

#bai4
def osc():
    for n in range(-3,5):
        print(n,end=" ")
        print(n*-1,end=" ")
    print()

#bai5
def ktsohoanthien(n):
    tong = 0
    for i in range(1,n):
        if (n % i) == 0:
            tong += i
    if tong == n: #nếu số thịnh vượng thì thay đổi tong != n
        return True
    else:
        return False
n= int(input("nhập số nguyên n:"))
if ktsohoanthien(n):
    print(n,"là số hoàn thiện")
else:
    print(n,"là số ko hoàn thiện")