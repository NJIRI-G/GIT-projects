print("Welcome to my Quiz")

playing = input("Do you want to play?  ")


if playing.lower() != "yes":
    quit()

print("Okay! lets play")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Thats correct!")
    score += 1
else:
    print("Wrong answer!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Thats correct!")
    score += 1
else:
    print("Wrong answer!")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Thats correct!")
    score += 1
else:
    print("Wrong answer!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Thats correct!")
    score += 1
else:
    print("Wrong answer!")

print("You got " + str(score)+ "  questions correct")
print("You got  " + str((score/4) * 100 ) + "%." )
