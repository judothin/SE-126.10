#jayden fagre
#01/17/24
#prompt: You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. Your
#report should look like the following sample output. The last line should print the number of
#computers in the file.


import csv
total_records = 0

#idk if this is needed but i added it when i was trying to figure out why it wasnt working
comp_type = []
manufacturer = []
processor = []
ram = []
hdd_1 = []
num_hdd = []
hdd_2 = []
os = []
year = []

import csv

with open ('W2\w2d2 hw\lab2b.csv') as csvfile:
    file = csv.reader(csvfile)

    #labels (yes i looked up how to line them up like this)
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Type", "Man", "Proc", "RAM", "HDD1", "HDD_NUM", "HDD2", "OS", "Year"))

    for rec in file:
        if rec[0] == "D":
            comp_type = "Desktop"
        elif rec[0] == "L":
            comp_type = "Laptop"
        else:
            comp_type = "ERROR"

        if rec[1] == "DL":
            manufacturer = "Dell"
        elif rec[1] == "GW":
            manufacturer = "GATEWAY"
        elif rec[1] == "HP":
            manufacturer = rec[1]
        else:
            manufacturer = "ERROR"

        processor = rec[2]
        ram = rec[3]
        hdd_1 = rec[4]
        num_hdd = rec[5]
        os = rec[6]
        year = rec[7]

        #figuring this out was annoying ngl
        if num_hdd == "1":
            hdd_2 = "N/A"
        elif num_hdd == "2":
            hdd_2 = rec[6]
            os = rec[7]
            year = rec[8]
        
        total_records += 1

        

        

    



        

        #final printed msg
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(comp_type, manufacturer, processor, ram, hdd_1, num_hdd, hdd_2, os, year))

#print total amount of records processed
print(f"Total number of records: {total_records}")