# info = {
#    "Name"  : "PRANTO",
#    "ID" : 2233081405,
#    "Department" : "CSE",
# }

# print(info)
# print(info["Name"])
# print(info["ID"])
# print(info["Department"])
# print(type(info))


# info["Name"] = "PRITOM" #Overwrite
# info["Surname"] = "KUMAR" #New adding
# print(info["Name"])
# print(info["Surname"])

#______________NESTED_______
student = {
   "Name" : "PRANTO",
   "subject" : {
      "Math" : 60,
      "Eng" : 70,
      "CSE" : 80,
   } 
}
print(student)
print(student["subject"])
print(student["subject"]["Math"])
print(student["subject"]["Eng"])
print(student["subject"]["CSE"])