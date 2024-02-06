print ("Pranto is my name.")
print ("My age is 20.")
print ("My Name is Pranto." , "I am 20 years Old.")
print (50)
print (10+30)
print (50-30)

#---------variables-------#

name = "PRITOM" ##String
age = 20
price = 25.67

print("name") ##output is name ;
print (name)  ##output is variables data ;
print (age)
print (price)

print ("My name is :",name)
print ("My age is :",age)

age2 = age 
print (age2)

#--------------Type-------------#

print(type(name)) ## type of variables;
print(type(age))
print(type(price))

#--------------Data Type-------------#
name1 = 'Pranto' ##string types
name2 = "PRITOM"
name3 = '''pranto'''

print(name1)
print(name2)
print(name3)

age3 = 20
old = False
a = None
print(type(old)) # boolean type
print(type(a)) # None type 

#--------------Comments-------------#

"""Multi line 
comments"""

# single line comments

#--------------Operators-------------#

#Arithmetics operators
a = 2
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #Reminder
print(a ** b) #a^b

#Relational operators 
a = 50
b = 20
print(a == b) # False
print(a != b) # True
print(a >= b) # True
print(a <= b) # False
print(a > b) # True
print(a < b) # False

#Assignment operators
num = 10 
num = num + 10 #10 + 10 => 20
print("Number is :",num)
num += 10 #increment =>30
print(num)
num -= 10 #Decrement => 20
print(num)
num *= 10 #multiply => 200
print(num)
num /= 10 #Divided => 20.0
print(num)
num %= 6  #Reminder => 2
print(num) 
num **= 2 #power => 4 
print(num) 

#Logical Operators
print(not False) #True
print(not True)  #False 
c = 10
d = 20 
print(not (c > d)) # True

val1 = True
val2 = False 
print("AND operator : ",val1 and val2) # Both same otherwise False
print("AND operator : ",(c != d) and (c < d)) 
print("OR operator : ",val1 or val2) # one should be true
print("OR operator : ",(c == d) or (c < d)) 

#--------------Type Convert-------------#
f = 10
g = 20.45

print(f+g)
#Type casting
j = int ("3")
print(type(j))
print(j+f) 
k = 4.50
l = str(k)
print(type(l))

#--------------Input-------------#
name = input("Enter your name: ")
age =int(input ("Enter your age: "))
print("Welcome",name)
print("Your age is:",age)
print(type(name),name)
print(type(age),age) # "20" , "10.00"
