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

#---------------------Main Code--------------------#

def difference(people, max_cap):
  if people <= max_cap:
      extra_people = max_cap - people
      print(f"It is legal to hold the meeting and there will be {extra_people} additional people that can legally attend.")
  else:
      excess_people = people - max_cap
      print(f"The meeting cannot be held as planned due to the standing fire regulations and {excess_people} people must be excluded in order to meet the fire regulations.")


def decision(response):
  while True:
    response = input("Do you want to check another meeting? (y/n) ")
    if response.lower() == "n":
        print("Thank you for using the program. Goodbye!")
        return False
    elif response.lower() == "y":
        return True
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

#calling functions
response = "y"
while True:
  max_cap = int(input("Enter the maximum room capacity: "))
  people = int(input("Enter the number of people attending the meeting: "))
  difference(people, max_cap)
  if not decision(response):
      break