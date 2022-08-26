x = int(input("size:"))
stu = []
record = []
for i in range (0,x):
    stu.append(input(""))
    stu.append(input())
    record.append(stu)
    stu = []  
print(record)
temp_record = []
for i in record:
    if i not in temp_record:
        temp_record.append(i)
record = temp_record
my_list = []
my_list.append(record.pop(record.index(max(record))))
x = record
print(max(x))