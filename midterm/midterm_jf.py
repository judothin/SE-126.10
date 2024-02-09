# jayden fagre
# 2/8/24
# description: A program that will allow you to see some of the best products related to mechanical keyboards.
# P.S. terminal has to be open on a little more than half the screen to be displayed nicely

# variable dictionary:
# name - list of prebuilt keyboard names
# brand - list of prebuilt keyboard brands
# price - list of prebuilt keyboard prices
# layout - list of prebuilt keyboard layouts
# switch - list of prebuilt keyboard switches
# lubed - list of prebuilt keyboard lubed status
# wireless - list of prebuilt keyboard wireless status
# hotswap - list of prebuilt keyboard hotswap status
# sname - list of switch names
# sprice - list of switch prices
# stype - list of switch types
# sbottomforce - list of switch bottom force
# gname - list of gaming keyboard names
# gbrand - list of gaming keyboard brands
# gprice - list of gaming keyboard prices
# glayout - list of gaming keyboard layouts
# gswitch - list of gaming keyboard switches
# gwireless - list of gaming keyboard wireless status
# ghotswap - list of gaming keyboard hotswap status
# gaming.text - file containing gaming keyboard data
# prebuilts.txt - file containing prebuilt keyboard data
# switchs.txt - file containing switch data
# view_all() - function to display best prebuilt keyboards
# best_switches() - function to display best switches
# gaming_keeb() - function to display best gaming keyboards


import csv

name = []
brand = []
price = []
layout = []
switch = []
lubed = []
wireless = []
hotswap = []
sname = []
sbrand = []
sprice = []
stype = []
sbottomforce = []
gname = []
gbrand = []
gprice = []
glayout = []
gswitch = []
gwireless = []
ghotswap = []

with open('midterm/prebuilts.txt', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for rec in reader:
        if rec: 
            name.append(rec[0])
            brand.append(rec[1])
            price.append(rec[2])
            layout.append(rec[3])
            switch.append(rec[4])
            lubed.append(rec[5])
            wireless.append(rec[6])
            hotswap.append(rec[7])

with open('midterm/switchs.txt', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for rec in reader:
        if rec: 
            sname.append(rec[0])
            sprice.append(rec[1])
            stype.append(rec[2])
            sbottomforce.append(rec[3])

with open('midterm/gaming.txt', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for rec in reader:
        if rec: 
            gname.append(rec[0])
            gprice.append(rec[1])
            glayout.append(rec[2])
            gswitch.append(rec[3])
            gwireless.append(rec[4])
            ghotswap.append(rec[5])

# func to display best gaming keyboards
def gaming_keeb():
    print("\n")
    print("Best Gaming Keyboards In Each Price Range:".center(100))
    print("\n")
    print("Name:".ljust(30) + "Price:".ljust(15) + "Layout:".ljust(15) + "Switch:".ljust(30) + "Wireless:".ljust(25) + "Hotswap:".ljust(30))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    for i in range(len(gname)):
        print(gname[i].ljust(30) + gprice[i].ljust(15) + glayout[i].ljust(15) + gswitch[i].ljust(30) + gwireless[i].ljust(25) + ghotswap[i].ljust(30))
        print()

# func to display best switches
def best_switches():
    print("\n")
    print("Outemu switches can be bought on aliexpress".center(100))
    print("(fyi outemus are insane for the price and silent versions are actually silent)".center(100))
    print("all others can be bought at loobedswitches.com:".center(100))
    print("\n")
    print("Name:".ljust(30) + "Price:".ljust(30) + "Type:".ljust(23) + "Bottom Force:".ljust(30))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    for i in range(len(sname)):
        print(sname[i].ljust(30) + sprice[i].ljust(30) + stype[i].ljust(23) + sbottomforce[i].ljust(30))
        print()

# func to display best prebuilt keyboards
def view_all():
    print("\n")
    print("Best Prebuilt Keyboards In order:".center(100))
    print("\n")
    print("Name:".ljust(30) + "Price:".ljust(15) + "Layout:".ljust(15) + "Switch:".ljust(30) + "Lubed:".ljust(15) + "Wireless:".ljust(15) + "Hotswap:".ljust(30))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    for i in range(len(name)):
        print(name[i].ljust(30) + price[i].ljust(15) + layout[i].ljust(15) + switch[i].ljust(30) + lubed[i].ljust(15) + wireless[i].ljust(15) + hotswap[i].ljust(30))
        print()
        

# menu
while True:
    print("\n1. View Best Prebuilt Keyboards \n2. View Best Switches \n3. View The Best Gaming Keyboards\n4. Exit\n")
    print(f"\n")
    choice = input("Enter your choice: ")
    if choice == '1':
        view_all()
    elif choice == '2':
        best_switches()
    elif choice == '3':
        gaming_keeb()
    elif choice == '4':
        break # dont get mad at the break...
    else:
        print("Invalid choice. Please try again.")



