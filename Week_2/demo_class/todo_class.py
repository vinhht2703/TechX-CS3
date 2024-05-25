# Mô tả bài tập:

# Hãy xây dựng một list sinh viên với các thuộc tính sau: mã sinh viên, tên sinh viên, điểm toán, điểm văn, điểm hóa.

# + Tạo list gồm 5 sinh viên

# + In thông tin các sinh viên có điểm trung bình lớn hơn 5

# + In ra các sinh viên có điểm hoá dưới 5

# Điền đường link nộp bài tập tại ô này:


class Student:
    def __init__(self, code, name, mathPoint, literaturePoint, chemistryPoint):
        self.code = code
        self.name = name
        self.mathPoint = mathPoint
        self.literaturePoint = literaturePoint
        self.chemistryPoint = chemistryPoint

    def getPointAvg(self):
        return (self.mathPoint + self.literaturePoint + self.chemistryPoint) / 3


student1 = Student(1, "Student 1", 10, 10, 10)
student2 = Student(2, "Student 2", 5, 6, 7)
student3 = Student(3, "Student 3", 1, 1, 1)
student4 = Student(4, "Student 4", 9, 8, 7)
student5 = Student(5, "Student 5", 5, 4, 3)

studentList = [
    student1,
    student2,
    student3,
    student4,
    student5,
]


def printStudentInfo(stud):
    print(
        f"\n- id: {stud.code} - name: {stud.name} - math: {stud.mathPoint} - literature: {stud.literaturePoint} - chemistry: {stud.chemistryPoint}"
    )


print("\nIn thông tin các sinh viên có điểm trung bình lớn hơn 5")
for stud in studentList:
    avgPoint = stud.getPointAvg()
    if avgPoint > 5:
        printStudentInfo(stud)
        print(f"Average point: {avgPoint}")

print("\n--------------------------------------------------------------------\n")
print("In ra các sinh viên có điểm hoá dưới 5")
for stud in studentList:
    if stud.chemistryPoint < 5:
        printStudentInfo(stud)
