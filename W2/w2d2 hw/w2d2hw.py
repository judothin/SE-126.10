#jayden fagre
#01/17/24
#prompt: You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. Your
#report should look like the following sample output. The last line should print the number of
#computers in the file.
#Organization of the csv file:


import csv
total_records = 0

with open ('lab2b.csv') as csvfile:
    file = csv.reader(csvfile)

    #for rec 0
    for rec in file:
        if rec[0] == "D":
            comp_type = "Desktop"
        elif rec[0] == "L":
            comp_type = "Laptop"
        else:
            comp_type = "ERROR"

    #for rec 1
        if rec[1] == "DL":
            manufacturer = "Dell"
        elif rec[1] == "gw":
            manufacturer = "GATEWAY"
        elif rec[1] == "HP":
            manufacturer = rec[1]
        else:
            manufacturer = "ERROR"

    #for all other recs
        processor = rec[2]
        ram = rec[3]
        hdd_1 = rec[4]
        num_hdd = rec[5]

    #final printed msg
        print(rec)
        print(f"{comp_type}       {manufacturer}        {processor}       {ram}       {hdd_1}       {num_hdd}       {hdd_2}       {os}       {year}")