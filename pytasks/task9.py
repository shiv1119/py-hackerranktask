n = int(input(""))
list1 = list(map(int, input().split()))
print(list1)
temp_list = []
for i in list1:
    if i not in temp_list:
        temp_list.append(i)
list1 = temp_list
my_list = []
my_list.append(list1.pop(list1.index(max(list1))))
x = list1
print(max(x))
   