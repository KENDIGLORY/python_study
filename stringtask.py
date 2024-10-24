name="   JOHn ."

name=name.replace("."," ")
name=name.strip()
print(name)
name=name.lower()
print(name)

sentence_one="The Dog Breed is German Shepherd"
print(sentence_one[8:23])
sentence_two="Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:30]) 

#split the sentence with a semicolon;
#use len to display the number of characters in the string
sent1="The lazy dog; ran so fast; it hit the wall."
sent2=sent1.split(";")
print(sent2)
print(len (sent2))

#replace the fullstop in first_name then strip and print
#replace the coma in last_name then strip and print
#concantenate first_name and last_name then print full_name
first_name=" joh.n"
last_name=" Do,e"
first_name=first_name.replace(".","")
first_name=first_name.strip()
print(first_name)
last_name=last_name.replace(",","")
last_name=last_name.strip()
print(last_name)
full_name=first_name+" "+last_name
print(full_name)

# first replace comma then replace the opening brackets
#replace the double quotation marks
#use single quotes(') to replace double quotes(" ")
#lastly replace the clossing brackets
r='["E","W","C"]'
r=r.replace(",","")
r=r.replace("[","")
r=r.replace('"',"")
r=r.replace("]","")
print(r)


#concatenation practice
first_name="glory"
last_name="kendi"
full_name=first_name+" "+last_name
print(full_name)

#indexing practice
#print the first and last characters 
word="PYTHON"
print(word[0])
print(word[5])

#slicing practice
#extract and print the word python
phrase="learning python is fun!"
print(phrase[9:15])

#character replacement
#replace "World" with "Python"
greet="Hello World"
greet=greet.replace("world","Python")
print(greet)

#print in uppercase and lowecase
num="Python Programming"
num=num.upper()
print(num)
num=num.lower()
print(num)

#count the occurance of letter s
txt="this is a simple sentence"
x=txt.count("s",0,24)
print(x)

#check substring pressence check if "future exists in the string" 
#usse keyword 'in' to check
text="the best way to predict the future it to create it"
print("future"in text)

#string length
txt="data science"
print(len(txt))

#remove white spaces
txt="  John Doe  "
txt=txt.strip()
print(txt)

#reversing a string print the reversed version
#using slicing method is easiest t=t[::-1]
txt="reverse this"
text= txt[::-1]
print(text)


#a = '''Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.'''
#print(a)

