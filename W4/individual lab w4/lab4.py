# Jayden Fagre, Lab 4
# 2/3/24
# Prompt: In Python, process the text file “lab4A_GOT_NEW.txt” to store each field into its own corresponding list: This means you will have 1D parallel lists for this file! 

import csv

fname = []
lname = []
age = []
nickname = []
house = []

with open ('W4\individual lab w4\lab4A_GOT_NEW.txt') as csvfile:
    reader = csv.reader(csvfile)

    for rec in reader:
        fname.append(rec[0])
        lname.append(rec[1])
        age.append((rec[2]))
        nickname.append(rec[3])
        house.append(rec[4])

print (f"{'First':<12} {'Last':<12} {'Age':<12} {'Nickname':<20} {'House'}")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for i in range(0, len(fname)):
    print (f"{fname[i]:<12} {lname[i]:<12} {age[i]:<12} {nickname[i]:<20} {house[i]}")


motto = []
lan = 0
tar = 0
bar = 0
sta = 0
nwa = 0
tul = 0

for i in range(0, len(house)):
    if house[i] == 'House Lannister':
        motto.append('Hear me roar!')
        lan += 1
    elif house[i] == 'House Targaryen':
        motto.append('Fire & Blood')
        tar += 1
    elif house[i] == 'House Baratheon':
        motto.append('Ours is the fury.')
        bar += 1
    elif house[i] == 'House Stark':
        motto.append('Winter is Coming')
        sta += 1
    elif house[i] == "Night's Watch":
        motto.append('And now my watch begins.')
        nwa += 1
    elif house[i] == 'House Tully':
        motto.append('Family. Duty. Honor.')
        tul += 1

print (f" \n")
print (f"{'First':12} {'Last':12} {'Age':12} {'Nickname':20} {'House':20} {'Motto'}")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for i in range(0, len(fname)):
    print (f"{fname[i]:12} {lname[i]:12} {age[i]:12} {nickname[i]:20} {house[i]:20} {motto[i]}")

print (f" \n")

print(f"House Lannister: {lan}")
print(f"House Targaryen: {tar}")
print(f"House Baratheon: {bar}")
print(f"House Stark: {sta}")
print(f"Night's Watch: {nwa}")
print(f"House Tully: {tul}")
print(f"Total number of people: {len(fname)}")

# needed the internet for this one, the average age wasnt working
average_age = sum(int(a) for a in age) / len(age)
print(f"Average Age: {average_age :.0f}")


    
    




