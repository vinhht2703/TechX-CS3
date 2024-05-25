# Trung tâm đào tạo lập trình Techx cần lưu trữ thông tin quản lý với các thông tin như sau:
# 1/ Học viên:
#  - Đối tượng: HocVien(maHV, tenHV, ngaySinh, khoaHoc)
#  - Phương thức:
#   + dangKyKhoaHoc(khoaHoc): Đăng ký một khóa học mới.
#   + hienThiKhoaHoc(): Hiển thị danh sách khóa học đã đăng ký.Khóa học:
# 2/ Khóa học:
#  - Đối tượng: KhoaHoc(maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi)
#  - Phương thức:
#   + thongTinKhoaHoc(): Hiển thị thông tin chi tiết về khóa học.
# Yêu cầu thực hiện:
#    + Tạo các lớp đối tượng cho Học viên, Khóa học.
#    + Định nghĩa các phương thức theo yêu cầu.
#    + Tạo một số đối tượng (ít nhất 2 học viên, 2 khóa học) và thực hiện một số thao tác trên chúng (đăng ký khóa học, hiển thị khóa học ).


class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi

    def thongTinKhoaHoc(self):
        print(
            f"Ma KH: {self.maKhoaHoc} - Ten KH: {self.tenKhoaHoc} - Hinh thuc: {self.hinhThuc} - Hoc phi: {self.hocPhi}\n"
        )


class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh, khoaHoc):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.dsKhoaHoc = [khoaHoc]

    def dangKyKhoaHoc(self, khoaHoc):
        dsKhoaHoc = self.dsKhoaHoc
        if type(dsKhoaHoc) is list:
            if khoaHoc not in dsKhoaHoc:
                dsKhoaHoc.append(khoaHoc)
                return print("Dang ky khoa hoc thanh cong!\n")
            else:
                return print("Ban da dang ky khoa hoc nay roi!\n")
        return print("Dang ky khoa hoc that bai!\n")

    def hienThiKhoaHoc(self):
        for khoaHoc in self.dsKhoaHoc:
            khoaHoc.thongTinKhoaHoc()


khoahoc1 = KhoaHoc("KH_1", "Ten khoa hoc 1", "offline", 20000)
khoahoc2 = KhoaHoc("KH_2", "Ten khoa hoc 2", "online", 50000)
khoahoc3 = KhoaHoc("KH_3", "Ten khoa hoc 3", "offline", 60000)
khoahoc4 = KhoaHoc("KH_3", "Ten khoa hoc 3", "offline", 60000)

hocvien1 = HocVien("HV_1", "Nguyen Van A", "23/12/1999", khoahoc1)
hocvien2 = HocVien("HV_2", "Pham Van B", "11/11/2000", khoahoc2)
hocvien3 = HocVien("HV_3", "Tran Thi C", "11/12/1989", khoahoc3)


print(f"\n ------------- Hoc vien {hocvien1.maHV} - {hocvien1.tenHV} -------------\n")
hocvien1.dangKyKhoaHoc(khoahoc2)
hocvien1.dangKyKhoaHoc(khoahoc3)
hocvien1.dangKyKhoaHoc(khoahoc1)
hocvien1.hienThiKhoaHoc()

print(f"\n ------------- Hoc vien {hocvien2.maHV} - {hocvien2.tenHV} -------------\n")
hocvien2.dangKyKhoaHoc(khoahoc4)
hocvien2.dangKyKhoaHoc(khoahoc4)
hocvien2.hienThiKhoaHoc()

print(f"\n ------------- Hoc vien {hocvien3.maHV} - {hocvien3.tenHV} -------------\n")
hocvien3.hienThiKhoaHoc()
