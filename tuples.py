marks=(100,130,160,190,200)
print(marks)
print(type(marks))
marks=list(marks)
print(type(marks))
marks[2]=1000
print(marks)
marks=tuple(marks)
print(marks)

days= ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
print(days)
#find wednesday using an index
print(days[2])
#find the length of the tuple
print(len(days))
#replace thursday with thur
#first convert to alist
days=list(days)
#replace thur
days[3]="thur"
#convert back to tuple
days=tuple(days)
#display
print(days)