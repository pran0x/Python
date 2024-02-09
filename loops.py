# count = 1
# while count <= 100 :
#    print("Hello",count)
#    count +=1    
# print(count-1) 

## REVERSE________
# j = 10
# while j >= 0 :
#    print(j)
#    j-= 1
   
# num = 1
# while num <= 100:
#    print(num)
#    num+=1


# digit = 100
# while digit >= 1 :
#    print(digit)
#    digit-=1

# num = 3
# i =  1
# while i <= 10 :
#    print(i*num)
#    i+=1 

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx <= (len(list)-1) :
#    print(list[idx])
#    idx+=1

# list = (1, 4, 9, 16, 25, 36, 49, 64, 81, 49,100)
# x = 49
# y= 0
# while y <= (len(list)-1) :
#    if(list[y] == x) :
#       print("Found the idx at",y)
#       break
#    else:
#       print("Finding...")   
#    y+=1       

# list = [1,2,3,"PRANTO","PRITOM"]

# for num in list:
#    print(num)

# str = "PRITOM PRANTO"
# for char in str:
#    if(char == 'O'):
#       print("O FOUND")
#       break
#    print(char)
# else:
#    print("END OF ERA")

# list = (1, 4, 9, 16, 25, 36, 49, 64, 81, 49,100)
# for x in list:
#    print(x)


###---------RANGE()__________##

# seq = range(1,100) ##(Start, STOP)
# for i in seq:
#    print(i)
   
# seq2 = range(2,12,2) ##(Start, STOP,step size)
# for i in seq2:
#    print(i)

# n = int(input("ENTER NUMBER : "))
# for i in range(1,11):
#    print(i*n)


# for i in range(1,10):
#    pass
# if i > 5 :
#    pass
# print("END")

n = 5
sum = 1
i = 1
# for i in range(1,n+1):
#    sum*=i
# print(sum)

while i<=n :
   sum*=i
   i+= 1
print(sum)