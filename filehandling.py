file = open ("myFile.txt","r")
print(file.read())

file2 = open("myFile2.txt","w")
file2.write("This an is awesome day")


try:
    file = open("myFile2.txt","r")
    print(file.read())
except FileNotFoundError:
    print("Oops! This file does not exist")
finally:
    print("Thank you for visiting")