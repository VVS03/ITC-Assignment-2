String = "Python is a case sensitive language"

#a. 
print(len(String))


#b.
print(String[::-1])


#c.
new_string = String[10:26]
print(new_string)


#d.
replace_string = "object oriented"

New_line = String.replace(new_string, replace_string)
print(New_line)


#e.
e = String.find("a")
print(e)


#f.
f = String.replace(" ","")
print(f)