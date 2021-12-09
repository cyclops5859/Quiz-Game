# Created by Cyclops!
import time

print("Welcome to my computer quiz!")
time.sleep(2)

print("Let's play :)")
score = 0
time.sleep(2)

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does IDLE stand for? ")
if answer.lower() == "Integrated Development and Learning Environment":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What starts with P and ends with Y, and it's 5 words? ")
if answer.lower() == "puppy":
    print('Correct!')
    score += 1

elif answer.lower() == "pussy":
    print('Incorrect but i like the way you think! ^_^')
    
else:
    print("Incorrect!")
    
print("")

print("You got " + str(score) + " questions correct!")
print("And you got " + str((score / 6) * 100) + "%.")
