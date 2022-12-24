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



def vd2():
    class tugiac():
        def __init__(self,ten,a,b,c,d):
            self.ten=ten
            self.a=a
            self.b=b
            self.c=c
            self.d=d
        def chuvi(self):
            return (self.a + self.b + self.c + self.d)

    class binhhanh(tugiac):
        pass
    
    bh1=binhhanh('bình hành',3,4,5,6)
    print('chu vi hình bình hành là: ',bh1.chuvi())

    tg1=tugiac('vuông',6,6,6,6)
    print('chu vi hình vuông là: ',tg1.chuvi())
vd2()

