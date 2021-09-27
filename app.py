#get the user input and convert it into a troy
user_input = str(input("Enter a Phrase: "))
#split the user input 
text = user_input.split()
#declare a new varirable to store the acronym 
a = " "

for i in text:
    a = a+str(i[0]).upper()
print(a)