class student:
   # name = "Pranto"
   Varsity = "Uttara University"
   #Default Constructor
   def __init__(self):
      pass 
   #Parameterized Constructor
   def __init__(self, name, roll, marks): #Self Construction
      self.Name = name #attributes
      self.roll = roll
      self.marks = marks 
      print("Adding new Student..")
   
   def welcome(self):
      print("Welcome Student,", self.Name)
   
   def ID(self):
      print("Roll:", self.roll)
      
   def CG(self):
      print("CSE :", self.marks)
   
s1 = student("Pritom", 2233081405, 90) #
s1.welcome()
print(s1.Varsity)
s1.ID()
s1.CG()
# print("\n\nName:",(s1.Name),"\nInstitute:",(s1.Varsity),"\nRoll:",(s1.roll),"\nMarks in CSE:",(s1.marks))
# print(s1.roll)
s2 = student("Jannat", 2233081404, 80 )
s2.welcome()
print(s2.Varsity)
s2.ID()
s2.CG()

s3 = student("jui" , 2233081406, 60)
s3.welcome()
print(s2.Varsity)
s3.ID()
s3.CG()

# print("\n\nName:",(s2.Name),"\nInstitute:",(s2.Varsity),"\nRoll:",(s2.roll),"\nMarks in CSE:",(s2.marks))