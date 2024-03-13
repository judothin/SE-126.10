# jayden fagre
# 03 / 12 / 2024
# description: In this program you will be able to browse a small list of keyboard switches and search for them by brand, name, type, and actuation force. and each set of data will be bubble sorted into alphabetical order.

import texttable

import csv

brand = []
name = []
stype = []
acforce = []

# Bubble sort for 'brand' list
def bubble(brand, name, stype, acforce):
    n = len(brand)
    for i in range(n):
        for j in range(0, n - i - 1):
            if brand[j].lower() > brand[j + 1].lower():
                brand[j], brand[j + 1] = brand[j + 1], brand[j]
                name[j], name[j + 1] = name[j + 1], name[j]
                stype[j], stype[j + 1] = stype[j + 1], stype[j]
                acforce[j], acforce[j + 1] = acforce[j + 1], acforce[j]
    return brand, name, stype, acforce

with open("final project\switches.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        brand.append(rec[0])
        name.append(rec[1])
        stype.append(rec[2])
        acforce.append(rec[3])

continue_program = True

while continue_program:

    print (f"\nMenu:")
    print ("1. Give me all the data")
    print ("2. Search by brand")
    print ("3. Search by name")
    print ("4. Search by type")
    print ("5. Search by actuation force")
    print ("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":

        brand, name, stype, acforce = bubble(brand, name, stype, acforce)

        print("\nHere is all the data:\n")
        print("{:<18} {:<18} {:<18} {:<18}".format("Brand", "Name", "Type", "Actuation Force"))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        for i in range(len(brand)):
            print("{:<18} {:<18} {:<18} {:<18}".format(brand[i], name[i], stype[i], acforce[i]))

    elif choice == "2":

        brand_name = input("Enter the brand name your searching for: ")
        found = []

        # bubble sort - sorts the list into alphabetical order by the name of the switch

        n = len(name)
        for i in range(n):
            for j in range(0, n - i - 1):
                if name[j].lower() > name[j + 1].lower():
                    name[j], name[j + 1] = name[j + 1], name[j]
                    brand[j], brand[j + 1] = brand[j + 1], brand[j]
                    stype[j], stype[j + 1] = stype[j + 1], stype[j]
                    acforce[j], acforce[j + 1] = acforce[j + 1], acforce[j]

        for i in range(len(brand)):
            if brand_name.lower() == brand[i].lower():
                found.append(i)

        if len(found) > 0:
            print(f"\nWe found {brand_name} in the following switches' info: \n")
            print("Here is their info:\n")
            print("{:<18} {:<18} {:<18} {:<18}".format("Brand", "Name", "Type", "Actuation Force"))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            for i in found:
                print("{:<18} {:<18} {:<18} {:<18}".format(brand[i], name[i], stype[i], acforce[i]))
        else:
            print(f"\nWe did not find any switches in {brand_name}\n")
            print(f"Please Try again. ")
    
    elif choice == "3":
        switch_name = input("Enter the switch name your searching for: ").lower()
        found = []

        for i in range(len(name)):
            if switch_name == name[i].lower():
                found.append(i)

        if len(found) > 0:
            print(f"\nWe found {switch_name} in the following switches' info: \n")
            print("Here is their info:\n")
            print("{:<18} {:<18} {:<18} {:<18}".format("Brand", "Name", "Type", "Actuation Force"))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            for i in found:
                print("{:<18} {:<18} {:<18} {:<18}".format(brand[i], name[i], stype[i], acforce[i]))
        else:
            print(f"\nWe did not find any switches in {switch_name}\n")
            print(f"Please Try again. ")

    elif choice == "4":
        switch_type = input("Enter the switch type your searching for: ").lower()
        found = []

        brand, name, stype, acforce = bubble(brand, name, stype, acforce)

        for i in range(len(stype)):
            if switch_type == stype[i].lower():
                found.append(i)

        if len(found) > 0:
            print(f"\nWe found {switch_type} in the following switches' info: \n")
            print("Here is their info:\n")
            print("{:<18} {:<18} {:<18} {:<18}".format("Brand", "Name", "Type", "Actuation Force"))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            for i in found:
                print("{:<18} {:<18} {:<18} {:<18}".format(brand[i], name[i], stype[i], acforce[i]))
        else:
            print(f"\nWe did not find any switches in {switch_type}\n")
            print(f"Please Try again. ")

            
    elif choice == "5":
        switch_force = input("Enter the actuation force your searching for: ").lower()
        found = []

        brand, name, stype, acforce = bubble(brand, name, stype, acforce)

        for i in range(len(acforce)):
            if switch_force == acforce[i].lower():
                found.append(i)

        if len(found) > 0:
            print(f"\nWe found {switch_force} in the following switches' info: \n")
            print("Here is their info:\n")
            print("{:<18} {:<18} {:<18} {:<18}".format("Brand", "Name", "Type", "Actuation Force"))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            for i in found:
                print("{:<18} {:<18} {:<18} {:<18}".format(brand[i], name[i], stype[i], acforce[i]))
        else:
            print(f"\nWe did not find any switches in {switch_force}\n")
            print(f"Please Try again. ")


    elif choice == "6":
        print("Goodbye!")
        continue_program = False