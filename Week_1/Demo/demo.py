#output
print("Hello World!!!!!")

#input
title = input("input sth: ")
print(title)

#condition
a = 1
b = 2
if a > b:
    c = 3
    d = 4
    print('a > b')
elif a == b:
    e = 5
    f = 6
    if e < f:
         print('e < f')

    print('a < b')

#loop
lstNumber = [1,4,5,6,9]
for i in lstNumber:
    c = 4
    f = 5
    print(i)

print(lstNumber[1])

#dictionary = object = hashtable
# key : value
dicts = {
    "id": 1,
    "name": "Vinh Huynh",
    "isHandsome": 1
}
print(dicts["name"])

# dict array
lstDicts = [
   {
    "id": 1,
    "name": "Vinh Huynh",
    "isHandsome": 1
},
 {
    "id": 2,
    "name": "Vinh Huynh 2",
    "isHandsome": 0
}
]

print(lstDicts[1]["name"])

#Create
lstDicts.append(1)
lstDicts.append("abc")
print(lstDicts[3])

#Read
lstDicts[1]["name"]

#Update
lstDicts[1]["name"] = "Vinh Huynh edited"
print(lstDicts[1]["name"])

#Delete
lstDicts.pop(3)

