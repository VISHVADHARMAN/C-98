f=open("test.txt")
filelines=f.read()
for line in filelines:
    print(line)

introstring="My Name is Vishva, I am 15 years old"
words=introstring.split(",")
print(words)

def greet(name):
    print("Hello, "+name+".How Are You?")

greet("Vishva")