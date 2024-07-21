import csv

data = [['In The Box', 'Handset, USB C Charge Cable (1m), Documentation'],
 ['Model Number', 'MTP03HN/A'],
 ['Model Name', 'iPhone 15'],
 ['Color', 'Black'],
 ['Browse Type', 'Smartphones'],
 ['SIM Type', 'Dual Sim(Nano + eSIM)']]

with open("myFile.csv","w+",newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
    
    file.seek(0)

    reader = csv.reader(file)
    for row in reader:
        print(row)


# with open("myFile.csv","r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
