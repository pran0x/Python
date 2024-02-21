class student:
   def __init__(self,name , marks):
      self.name = name
      self.marks= marks
   
   @staticmethod #decorator #Class level method
   def hello():
      print("Hello")
         
   def get_avg(self):
      sum = 0
      for val in self.marks:
         sum += val
      print("Hi!", self.name,"\nyour avg score is:",sum/3)

       
s1= student("Tony",[98,97,96])
s1.hello() 
s1.get_avg()  
s1.name = "Stark"
s1.get_avg()