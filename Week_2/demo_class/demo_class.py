# variable
## title = "hello"

# function
## def getTitle

# hash table
object = {"id": 123, "name": "abc"}

# class: lớp đối tượng
## property - variable in class: thuộc tính
## method - function in class: phương thức

# instance: đối tượng

# --------------------------------------------------------------------

# product class:
## properties: id, name, price
## method: print product info, cal discount ex: price * 5


# construction: hàm tạo - gán giá trị khai báo đối tượng
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def getProdInfo(self):
        print(f"- id: {self.id} \n- name: {self.name} \n- price: {self.price}")

    def calDiscount(self, percent):
        return self.price * percent

    # price + % discount
    def calSale(self):
        discount = self.calDiscount(10)
        return self.price + discount


product = Product(1, "book", 10000)

product.getProdInfo()
print(product.calDiscount(20))
print(product.calSale())


print("\n--------------------------------------------------------------------\n")


class Staff:
    def __init__(self, code, name, basicSalary, position, coefSalary):
        self.code = code
        self.name = name
        self.basicSalary = basicSalary
        self.position = position
        self.coefSalary = coefSalary

    def calSalary(self):
        return self.basicSalary * self.coefSalary


class CEO(Staff):
    def __init__(self, code, name, basicSalary, position, coefSalary, bonus):
        super().__init__(code, name, basicSalary, position, coefSalary)
        self.bonus = bonus

    def calActualSalary(self):
        return self.calSalary() + self.bonus


class Manager(Staff):
    def __init__(self, code, name, basicSalary, position, coefSalary, minusBonus):
        super().__init__(code, name, basicSalary, position, coefSalary)
        self.minusBonus = minusBonus

    def calActualSalary(self):
        return self.calSalary() - self.minusBonus


staff = Staff(1, "Staff Name", 10, "staff", 0)
print(staff.calSalary())

ceo = CEO(2, "CEO Name", 20, "CEO", 2, 100)
print(ceo.calActualSalary())

manager = Manager(3, "Manager Name", 20, "Manager", 5, 200)
print(manager.calActualSalary())
