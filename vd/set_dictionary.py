'''Set trong python là một tập các giá trị không có thứ tự.
Mỗi giá trị trong set là duy nhất, không thể lặp lại và bất biến
( tức bạn không thể thay đổi giá trị các phần tử trong set). Tuy nhiên các set có thể thay đổi.
Chúng ta có thể thêm, xóa các phần tử trong set.'''
def set():
    monhoc = {'toán','lý','hóa','hóa','sinh'}
    monhoc.add('anh văn')#thêm phần tử vào set(note)
    monhoc.remove('sinh')#xóa-----------hoặc sài discard sẽ hạn chế bị lỗi                    
    monhocphu = {'gym','SQL','guitar','anh văn'}
    monhoc.update(monhocphu)#thêm nhiều phần tử vào set(note)
    print(monhoc)
    for i in monhoc:
        print(i)





'''Kiểu dữ liệu Dictionary trong Python là một tập hợp các cặp 'key' : 'value' không có thứ tự,
 có thể thay đổi và lập chỉ mục (truy cập phần tử theo chỉ mục)'''     #từ phiên bản py 3.7 thì có thứ tự
def dic():
    sinhvien={
        'họ tên':'Huỳnh thuận',
        'mã sv':'2211038',
        'điểm TB':'9.2'
    }
    #cặp nhật giá trị
    sinhvien['điểm TB'] ='9.5'    
    sinhvien.update({'họ tên':'huỳnh chí phi thuận','điểm TB':'9.7'})
    #thêm căp keys:value
    sinhvien.update({'nơi sinh':'hậu giang'})
    #xóa
    sinhvien.pop('mã sv')
    print(sinhvien)
    #duyệt các cặp khóa - giá trị:
    for x,y in sinhvien.items():
        print(x,y)

def tuvung():
    dic={'easy':'dễ',
    'cute':'dễ thương',
    'song':'bài hát'}
    a=input('nhập từ muốn dịch: ')
    print(dic.get(a,'không tìm thấy'))
tuvung()
