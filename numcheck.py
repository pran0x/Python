with open("nums.txt", "w") as x:
   data = x.write("1,2,35,55,86,76")


def check_EVEN_NUMS():
   with open("nums.txt","r") as new:
      new_data = new.read()
      num = "" 
      for i in range(len(new_data)):
         if((new_data[i] == ",")):
            print(num)
            num = ""
         else:
            num += new_data[i]
      
check_EVEN_NUMS()

with open("nums.txt", "r") as f:
   new_data = f.read()
nums = new_data.split(",")
print(nums)
count = 0
for val in nums:
   if(int(val) %2 == 0):
      print(val)
      count += 1 
      
print(count) 