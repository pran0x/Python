def fileWrite(): #A function to write to a file
  with open("File.txt", "w") as file:
    file.write("Wifi SSID Holder.\n")
    
#A Function to Read a file
def fileRead():
  with open("File.txt", "r") as file:
    print(file.read())
    file.seek(0) # Move the itr to start of the file
    content = file.read()
    print(content)

#A function to write and Read to a file;
def fileWriteRead():    
  with open("FileReadWrite.txt","w+") as  RW:
    RW.write("Wifi Name: \t")
    RW.write("Password : \n")
    RW.seek(0)
    print(RW.read())
#Function Calling
fileWriteRead()
fileRead()
fileWrite() 
    
    
    
    
    
    