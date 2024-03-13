#Name - Andy Ho, Hendry Reyes, Jayden Fagre

#Week 8 Class Lab

#Program Prompt - Write a Python program to assign passengers seats in an airplane.  Assume a small airplane with seat numbering as follows.
#Row
#1        A  B             C  D
#2        A  B             C  D
#3        A  B             C  D
#4        A  B             C  D
#5        A  B             C  D
#6        A  B             C  D
#7        A  B             C  D
#The program should display the seat pattern, with an ‘X’ making the seats already assigned. For example, after seats 1A, 2B and 4C are taken the display should look like this:
#Row
#1        X  B             C  D
#2        A  X             C  D
#3        A  B             C  D
#4        A  B             X  D
#5        A  B             C  D
#6        A  B             C  D
#7        A  B             C  D
#After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated.  This continues until all seats are filled or until the user signals that the program should end.  If a user types in a seat that is already assigned, the program should say that the seat is occupied and ask for another choice.
#You must use functions that allows the user to enter the row and seat number.  The row should be asked for separately from the seat number (two inputs
#You must use a function that asks the user in they want to continue or stop. The function should only accept an uppercase or lowercase y or n

#Variable Dictionary:
#seatA - list of A seats 
#seatB - list of B seats 
#seatC - list of C seats 
#seatD - list of D seats

#row_get() - function that will get the row choice from the user
#row_choice - variable that will store the row choice

#seat_get() - function that will get the seat choice from the user
#acceptable_seats - list of acceptable seats
#seat_choice - variable that will store the seat choice

#more_seats() - function that will ask the user if they want to continue to add more seats
#choice - variable that will store the choice of the user

#answer - variable that will store the choice of the user if they want to continue to add more seats
#row - variable that will store the row number

#row_input - variable that will store the row choice
#seat_input - variable that will store the seat choice

#---------------------PROGRAM BEGINS BELOW-------------------------------


#-----------------------LISTS---------------------------------------------
#create all the seats in a list
seatA = ["A", "A", "A", "A", "A", "A", "A"]
seatB = ["B", "B", "B", "B", "B", "B", "B"]
seatC = ["C", "C", "C", "C", "C", "C", "C"]
seatD = ["D", "D", "D", "D", "D", "D", "D"]


#--------------------------FUNCTIONS----------------------------------------
def row_get():#function will get the row choice from the user
    row_choice = -1 #initalize the row

    while row_choice < 1 or row_choice > 7:
        try:
            row_choice = int(input("\t\tEnter the ROW you wish to sit in [1-7]"))
            if row_choice < 1 or row_choice > 7:
                print("\t\tNOT A VALID ROW, PLEASE ENTER A VALID ROW [1-7]")
        except:#will not show an error if you enter a string(ex:letter) but will ask you to enter a valid row choice
            print("\t\tNOT A VALID ROW, PLEASE ENTER A VALID ROW [1-7]")
    
    
    return row_choice




def seat_get():#function will get the seat choice from the user
    acceptable_seats = ["A", "B", "C", "D"]

    seat_choice = input("\t\tEnter the SEAT you wish to sit in:").upper()

    while seat_choice not in acceptable_seats:#will only accept actual seats
        seat_choice = input("\t\tEnter the SEAT you wish to sit in [A/B/C/D]:").upper()

    return seat_choice
def more_seats():#ask the user if they want to continue to add more seats
    choice = input("\t\tDo you want to continue to add more seats [Y/N]:").upper()

    return choice

#-----------------------MAIN CODE BEGINS BELOW--------------------------

answer = "Y"

while answer.upper() == "Y":
    print("\t\t--------------------------------------------------")
    print("\t\t\t ROW")
    for i in range (0,7):
        row = i + 1
        print(f"\t\t | \t", i + 1, "\t", seatA[i], " ", seatB[i], "\t\t\t", seatC[i], " ", seatD[i], "\t |")#will print the seating map
    print("\t\t---------------------------------------------------")

    row_input = row_get()#returns the row choice
    seat_input = seat_get()#returns the seat choice

    print(f"\t\tYou have chosen: ROW:{row_input} SEAT:{seat_input}")
   
    if seat_input == "A":#seatlistA
        #This will take away the A seat in that row once chosen and will display a "x"
        if seatA[row_input - 1] != "X":
            seatA[row_input - 1] = "X"
        else:
            print(f"\t\tSorry but {row_input}{seat_input} has already been taken")
    elif seat_input == "B":#seatlistB
        #This will take away the B seat in that row once chosen and will display a "x"
        if seatB[row_input - 1] != "X":
            seatB[row_input - 1] = "X"
        else:
            print(f"\t\tSorry but {row_input}{seat_input} has already been taken")
    elif seat_input == "C":#seatlistC
        #This will take away the C seat in that row once chosen and will display a "x"
        if seatC[row_input - 1] != "X":
            seatC[row_input - 1] = "X"
        else:
            print(f"\t\tSorry but {row_input}{seat_input} has already been taken")
    elif seat_input == "D":#seatlistD
        #This will take away the D seat in that row once chosen and will display a "x"
        if seatD[row_input - 1] != "X":
            seatD[row_input - 1] = "X"
        else:
            print(f"\t\tSorry but {row_input}{seat_input} has already been taken")


    if seatA[i] == "X" and seatB[i] == "X" and seatC[i] == "X" and seatD[i] == "X":#if all seats were taken
        answer = "N"
    else:
        answer = more_seats()
#exit loop and program
print("\t\t Thank You For Using This Program")

