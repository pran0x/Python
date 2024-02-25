class person:
   name = "PRANTO"
   
   def __hello(self):
      print("Hello Person!")
      
   def welcome(self):
      self.__hello()
      
p1 = person()
# print(p1.__hello())
p1.welcome()      
 
class person3:
   name = "PRITOM"
   def __init__(self, name):
      self.name = name
   @classmethod  
   def person2(cls,name):
      cls.name = name
      print(cls.name)  
     
name1 = person3()   
print(person3.name)
name1.person2("Pranto")
print(name1.name)
# name1.person2()

class portal:
   
   @staticmethod
   def start(): ##Method
      print("Searching...")
   
   @staticmethod   
   def stop():
      print("Not Found.")
      
class ID:
   def __init__(self,roll):
      self.roll = roll

class student(portal,ID):
   def __init__(self, name):
      self.name = name
      # super().__init__(roll)
      # super().start()
      
class Institute(student):
   def __init__(self,varsity,name):
      self.varsity = varsity
      super().__init__(name)
      # super().__init__(roll) 
      super().start()

   

# s2 = student("Pranto", 2233081405)
# print(s2.roll)
# print(s2.name)
s3 = Institute(
   "UttaraUniversity",
   "PRANTO")

print(s3.varsity)
print(s3.name)
# print(s3.roll)
# print(s2.varsity)

class student:
   def __init__(self,math, chem,phy,eng):
         self.math = math
         self.chem = chem
         self.phy  = phy
         self.eng  = eng
         # self.percentage = str((self.math + self.chem + self.phy + self.eng) / 4) + "%"
   @property
   def percentage(self):
      return   str((self.math + self.chem + self.phy + self.eng) / 4) + "%"


s1 = student(98,99,97,90)
print(s1.percentage)
s1.phy = 80          
print(s1.percentage)