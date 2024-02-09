# def show(n): #Function Definition 
#    if (n == 0 ): #base case
#       return None
#    print(n)
#    show(n-1) #recursion
#    print("END")
# show(4) #Calling


# def fact (x):
#    if(x == 0 or x == 1):
#       return 1
#    else:
#       return x*fact(x-1) 
   
# print("Fact is :",fact(5))

# def calculate (n):
#    if(n == 0):
#       return 0
#    else:
#       print(n)
#       return calculate(n-1) + n 
# # calculate(5)
# sum = calculate(10)
# print(sum) 

def print_list(list, idx ):
   if (idx == len(list)):
      return 0
   print(list[idx])
   print_list(list, idx+1)
   
list = ["a", "b", "c", "d","e"]
print_list(list,0) 