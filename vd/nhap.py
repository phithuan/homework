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
vd1()