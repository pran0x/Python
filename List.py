marks = [45, 65.8, 46.78, 90, 20]
print(marks)
print(type(marks))
marks[0] = 89
print(marks[0])
list = [1,2,3]
list.append(4) #Adds one element at the end;
print(list)

nums = [4,6,3,7,1]
nums.sort() #Ascending order;
print(nums)
nums.sort(reverse=True) #Descending Order;
print(nums)

names = ["PRANTO" , "JUI"]
names.sort()
print(names)
names.sort(reverse= True)
print(names)

char = ["A", "C", "F", "K", "J", "P"]
char.reverse() #Reverse list;
print(char)

number = [1 , 3, 5 ]
number.insert(1,6)
number.insert(0,9) # Index element at index;
print(number) 
number.remove(5) # Remove the first digit of elements
print(number)
number.pop(0) # Remove the index elements
print(number)