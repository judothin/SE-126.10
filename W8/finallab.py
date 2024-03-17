# jayden fagre
# 03 / 14 / 2024

# prompt: Write a program that can be used by a small theater to sell tickets for performances. The theater’s auditorium has 15 rows of seats with 30 seats in each row. The program should display a screen that shows which seats are available and which are taken. Seats thar are available are represented by # and seats that are taken are represent by a *. There are aisles after seats H and V.

# variable dictionary:

# seatA - Seat4 - list of all the seats
# row_get() - function that will get the row choice from the user
# row_choice - variable that will store the row choice
# seat_get() - function that will get the seat choice from the user
# acceptable_seats - list of acceptable seats
# seat_choice - variable that will store the seat choice
# view_tsales() - function that will display the total ticket sales
# sold_seats - list of all the sold seats
# sales_info() - function that will display the total sales info
# total_cost - variable that will store the total cost of the tickets
# sold_seats - variable that will store the total amount of sold seats
# checkout() - function that will display the total cost of the tickets and checkout
# menu() - function that will display the menu
# choice - variable that will store the choice of the user
# seating_chart - list of all the seats
# codets - variable that will store if the user wants to continue or stop
# row_input - variable that will store the row choice
# seat_input - variable that will store the seat choice







# create lists
seatA = ["#"] * 15
seatB = ["#"] * 15
seatC = ["#"] * 15
seatD = ["#"] * 15
seatE = ["#"] * 15
seatF = ["#"] * 15
seatG = ["#"] * 15
seatH = ["#"] * 15
seatI = ["#"] * 15
seatJ = ["#"] * 15
seatK = ["#"] * 15
seatL = ["#"] * 15
seatM = ["#"] * 15
seatN = ["#"] * 15
seatO = ["#"] * 15
seatP = ["#"] * 15
seatQ = ["#"] * 15
seatR = ["#"] * 15
seatS = ["#"] * 15
seatT = ["#"] * 15
seatU = ["#"] * 15
seatV = ["#"] * 15
seatW = ["#"] * 15
seatX = ["#"] * 15
seatY = ["#"] * 15
seatZ = ["#"] * 15
seat1 = ["#"] * 15
seat2 = ["#"] * 15
seat3 = ["#"] * 15
seat4 = ["#"] * 15

# create functions
def row_get():
    row_choice = -1

    while row_choice < 1 or row_choice > 15:
        try:
            row_choice = int(input("\t\tEnter the ROW you wish to sit in [1-15]"))
            if row_choice < 1 or row_choice > 15:
                print("\t\tNOT A VALID ROW, PLEASE ENTER A VALID ROW [1-15]")
        except:
            print("\t\tNOT A VALID ROW, PLEASE ENTER A VALID ROW [1-15]")
    
    
    return row_choice

def seat_get():
    acceptable_seats = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4"]

    seat_choice = input("\t\tEnter the SEAT you wish to sit in: ").upper()

    while seat_choice not in acceptable_seats:
        seat_choice = input("\t\tEnter the SEAT you wish to sit in: ").upper()

    return seat_choice

def view_tsales(seating_chart):
    row_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

    sold_seats = []

    for i, row in enumerate(seating_chart): # enumerate returns the index and the value
        for j, seat in enumerate(row):
            if seat != "#":
                sold_seats.append(f"{row_names[i]}{chr(65 + j)}") # chr(65 + j) returns the letter of the seat

    print("Here's a list of all seats that have been sold: " + ', '.join(sold_seats)) # join the list of sold seats into a string


def sales_info(seating_chart):
    total_cost = 0
    sold_seats = 0

    for i, row in enumerate(seating_chart):
        for seat in row:
            if seat == "X":
                sold_seats += 1
                if i < 5:
                    total_cost += 200
                elif i < 10:
                    total_cost += 175
                else:
                    total_cost += 150

    print(f"Total seats sold: {sold_seats}")
    print(f"Total sales: ${total_cost}")
    return total_cost

def checkout(seating_chart):
    total_cost = sales_info(seating_chart)
    print(f"Your purchase of ${total_cost} was successful. Have a nice day!")

def menu():
    # initialize the seating chart outside of the loop
    seating_chart = [['#' for _ in range(30)] for _ in range(15)] # create a 2D list of 15 rows and 30 seats
    codets = True

    while codets:
        print("\n1. Purchase seat(s)")
        print("2. View total ticket sales")
        print("3. View sales info")
        print("4. Checkout")
        print("5. Quit")

        choice = input("\nPlease enter your choice: ")

        if choice == "1":
            print("\t\t--------------------------------------------------------------------------------------------------------------------")
            print("\t\t\t ROW\t\tSEATS")
            print("\t\t\t\t" + '   '.join([chr(65 + i) if i < 26 else str(i - 25) for i in range(30)])) # print the seat letters and numbers (fancy because non fancy/long way wasnt lining it up right and it was annoying)
            for i in range(15):
                print(f"\t\t | \t{i+1}\t" + '   '.join(seating_chart[i]) + "\t |") # print the seating chart
            print("\t\t--------------------------------------------------------------------------------------------------------------------")

            row_input = row_get()
            seat_input = seat_get()

            print(f"\t\tYou have chosen: ROW:{row_input} SEAT:{seat_input}")
            
            if seat_input in [chr(65 + i) if i < 26 else str(i - 25) for i in range(30)]: # check if the seat is valid
                if seating_chart[row_input - 1][ord(seat_input) - 65 if 'A' <= seat_input <= 'Z' else int (seat_input) + 25] != "X": # check if the seat is available
                    seating_chart[row_input - 1][ord(seat_input) - 65 if 'A' <= seat_input <= 'Z' else int(seat_input) + 25] = "X" # mark the seat as taken
                else:
                    print(f"\t\tSorry but {row_input}{seat_input} has already been taken")
            else:
                print("\t\tInvalid seat choice. Please enter a valid seat.")

        elif choice == "2":
            view_tsales(seating_chart)
        elif choice == "3":
            sales_info(seating_chart)
        elif choice == "4":
            checkout(seating_chart)
        elif choice == "5":
            print("Thank you for using my code!")
            codets = False
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")



# main code
menu()    

