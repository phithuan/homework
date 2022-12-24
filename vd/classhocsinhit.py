def nhap():
    for i in range(n):
        a[i]=hocsinh(0,0,0,0,)
        print('nhập học sinh thứ:',i+1)
        a[i].ten=input('nhập tên: ')
        b[i].lop=input('nhập lớp: ')
        c[i].diem=float(input('nhập điểm: '))
        d[i].truong=input('nhập trường: ')

def xuat():
    for i in range(n):
        a[i].show()

def diemmax():
    dmax=a[0].diem
    imax=0
    for i in range(n):
        if a[1].diem>damx:
            dmax=a[i].diem
            imax=i
        a[imax].show()

def sxtang():
    for i in range(n):
        for j in range(i):
            if a[i].diem<a[j].diem:
                a[i].diem,a[j].diem=a[j].diem,a[i].diem
                a[i].ten,a[j].ten=a[j].ten,a[i].ten
                a[i].lop,a[j].lop=a[j].lop,a[i].lop
                a[i].truong,a[j].truong=a[j].truong,a[i].truong
    xuat()


def sxgiam():
    for i in range(n):
        for j in range(i):
            if a[i].diem>a[j].diem:
                a[i].diem,a[j].diem=a[j].diem,a[i].diem
                a[i].ten,a[j].ten=a[j].ten,a[i].ten
                a[i].lop,a[j].lop=a[j].lop,a[i].lop
                a[i].truong,a[j].truong=a[j].truong,a[i].truong
    xuat()

def diem9():
    for i in range(n):
        if a[i].diem>=9:
            a[i].show()

def hocsinh():
    class Hocsinh():
        def __init__(self,ten,lop,diem,truong):
            self.ten=ten
            self.lop=lop
            self.diem=diem
            self.truong=truong

        def show(self):
            print('tên: ',self.ten)
            print('lớp: ',self.lop)
            print('điểm: ',self.diem)
            print('trường: ',self.truong)
            print('==========================')
while True:
    print('chọn số đi 0-6')
    chon=int(input('mời m chọn chức năng:'))
    if chon==1:
        n=int(input('nhập số học sinh cần quản lý'))
        a=[0]*n
        nhap()
    if chon==2:
        xuat()
    if chon==3:
        diemmax()
    if chon==4:
        sxtang()
    if chon==5:
        sxgiam()
    if chon==6:
        diem9()
    if chon==0:
        break
