#------------String-Concatenation------------#
str1 = "PRITOM"
str2 = "PRANTO"
print(str1 + str2)
final_str = str1 + str2
print (final_str)  
print (str1[2])
str3 = "PRITOM PRANTO"
#-------01234567891011
print(str3[2:]) #starting index : Ending index
print(str3[3:6]) ##TOM . 

#________BACKWARD STRING_____________
print(str3[-6:-2]) # To the End -6,-5,-4,-3

#------------String Function------------#

str = "pritom Plays Call of duty Warzone"
print(str.endswith("one")) #Ends with this substring->True

print(str.capitalize())
print(str)
str1 = str.capitalize()
print(str1)

str3 = "Python is better then javaScript!"
print(str3.replace("Python" , "Rust")) #Old , new [Replace]

print(str3.find("o")) # Find "o" Index
print(str3.count("t")) # Count numbers of string "t"