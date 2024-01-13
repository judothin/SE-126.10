#jayden fagre
#Lab 1
#1/11/24

#prompt: You will be writing one Python file for this project - it is a program that determines whether a 
#meeting room is in violation of fire regulations regarding the maximum room capacity. The
#program will accept the maximum room capacity and the number of people attending the
#meeting. If the number of people is less than or equal to the maximum room capacity, the
#program announces that it is legal to hold the meeting and tells how many additional people may
#legally attend. If the number of people exceeds the maximum room capacity, the program
#announces that the meeting cannot be held as planned due to the fire regulation and tells how
#many people must be excluded in order to meet the fire regulations. The user should be allowed
#to enter and check as many rooms as they would like without exiting the program.

#--------------------------------------Main Code--------------------------------------------------------#

def calculate_difference(attendees, capacity):
    difference = attendees - capacity
    return difference

def decision ():
    response = input("Would you like to Enter the attendance for another meeting? (y/n) ").lower()
    return response
response = decision()
mname = input("What is the name of the meeting? ")
decision (response)
attendees = int(input("How many people are attending the meeting? "))
capacity = int(input("What is the capacity of the room? "))

if attendees <= capacity:
    print("It is legal to hold the meeting. You may have", calculate_difference(capacity, attendees), "more people attend.")

else:
    print("The meeting cannot be held as planned due to fire regulations. You must exclude", calculate_difference(attendees, capacity), "people to meet the fire regulations.")

response = decision()

if response == "y":
    mname = input("What is the name of the meeting? ")
    attendees = int(input("How many people are attending the meeting? "))
    capacity = int(input("What is the capacity of the room? "))

else:
    print("Thank you for using the meeting room calculator. Have a nice day!")
    
    