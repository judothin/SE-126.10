# jayden fagre
# 02 / 21 / 24
# prompt: In this lab, you will build a Python application that allows a user to repeatedly choose an option from a menu to search through the data provided in the text file below. You will perform both sequential search as well as binary search. See the lab prompt for further details. 



import csv

id_stud = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []

with open ("W7\lab 5\lab5_students.txt") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        id_stud.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

continue_program = True

while continue_program:
    # menu
    print(f"\nMenu:")
    print("1. Search by class 1")
    print("2. Search by class 2")
    print("3. Search by class 3")
    print("4. Search by last name")
    print("5. Search by student ID")
    print("6. Exit")

    
    choice = input("Enter your choice (1-6): ")


    if choice == "1":
        # sequential search
        class_name = input("Enter the class 1 name your searching for: ")
        found = []

        for i in range (len(class1)):
            if class_name.lower() == class1[i].lower():
                
                found.append(i)

        if len(found) > 0:
            print (f"\nWe found {class_name} in the following students' info: \n")

            for i in found:
                print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(fname[i], lname[i], id_stud[i], class1[i], class2[i], class3[i]))
        else: 
            print (f"\nWe did not find any student in {class_name}\n")
            print (f"Please Try again. ")

    elif choice == "2":
        class2_name = input("Enter the class 2 name your searching for: ")
        # sequential again
        found = []

        for i in range (len(class2)):
            if class2_name.lower() == class2[i].lower():
                
                found.append(i)

        if len(found) > 0:
            print (f"\nWe found {class2_name} in the following students' info: \n")

            for i in found:
                print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(fname[i], lname[i], id_stud[i], class1[i], class2[i], class3[i]))
        else: 
            print (f"\nWe did not find any student in {class2_name}\n")
            print (f"Please Try again. ")

    elif choice == "3":

        class3_name = input("Enter the class 3 name you're searching for: ").lower()

        # binary search
        min = 0
        max = len(class3) - 1
        bin_count = 0
        found = False

        while min <= max:
            bin_count += 1
            mid = (min + max) // 2
            if class3[mid].lower() < class3_name:
                min = mid + 1
            elif class3[mid].lower() > class3_name:
                max = mid - 1
            else:
                print (f"\nWe found {class3_name} at index position {mid}")
                print (f"\tHere is their info: ")
                print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(fname[mid], lname[mid], id_stud[mid], class1[mid], class2[mid], class3[mid]))
                found = True
                min = max + 1

        if not found:
            print(f"\n{class3_name} was not found in the list.")
            print(f"Please try again.")
        
    elif choice == "4":
        
        last_name = input("Enter the last name your searching for: ")

        # sequential search
    
    elif choice == "5":

        student_id = input("Enter the student ID your searching for: ")

        # sequential search
        found = []

        for i in range (len(id_stud)):
            if student_id.lower() == id_stud[i].lower():
                found.append(i)

        if len(found) > 0:
            print (f"\n We found {student_id} at index position {found[0]}")
            print (f"\tHere is their info: ")

            for i in range (len(found)):
                print (f"\t\t{fname[found[i]]} \t {lname[found[i]]} \t {id_stud[found[i]]} \t {class1[found[i]]} \t {class2[found[i]]} \t {class3[found[i]]}\n")
        else: 
            print (f"\nWe did not find {student_id} in the file\n")
            print (f"Please Try again. ")

    elif choice == "6":
        print("gooooooo bye.")
        continue_program = False

    else:
        print("Invalid choice. Please try again.")