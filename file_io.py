# f = open("demo.txt","r")
# data = f.readlines()
# print(data)
# print(type(data))
# f.close()

# with open("demo.txt","r") as f:
#    data = f.read()
#    print(data)
   
# with open("demo.txt","w") as f:
#    data = f.write("new Data")
#    print(data)    

# import os
# os.remove("demo.txt")


New = open("new text.txt", "w")
data = New.write("Hi everyone")
New = open("new text.txt", "a+")
data = New.readline()
data = New.write("\nWe are learning File I/O")
data = New.readline()
data = New.write("\nUsing Java")
data = New.readline()
data = New.write("\nI like programming in Java")
data = New.readline()
New = open("new text.txt","r")
data = New.read()
print(data)
New.close()

# new_data = data.replace("Java", "Python")
# print(new_data)
# if (data.find("learning") != -1):
#    print("Found")
# else:
#    print("not Found")
def check_for_line():
      word = "Java"
      line_number = 1   
      data = True
      with open("new text.txt","r") as New:
         while data:
            data = New.readline()
            if(word in data):
               print(line_number)
               return
            line_number += 1
      return -1
   
print(check_for_line()) 
