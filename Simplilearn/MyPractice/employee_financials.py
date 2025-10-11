print('Employee Finanaial Data')
# Collect user input
name = input("Enter emloyee name: ")
department = input("Enter employee department: ")
experience = int(input("Enter years of experience: "))
salary = float(input("Enter the salary ($): "))

print(f"Employee Name : ",name)
print(f"Employee Department : ",department)
print(f"Employee Experience : ",experience)
print(f"Employee Salary : ",salary)


my_list1=[10,20]
my_list2=[30,40]

my_list3=[50,60]
my_list4=[70,80]

my_list1.append(my_list2)
my_list3.extend(my_list4)
print(my_list1)
#print(my_list1[2][1])
print(my_list3)