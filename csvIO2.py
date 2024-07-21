import csv
data = [
    {"id":101,"name":"ravi","marks":100},
    {"id":102,"name":"rohit","marks":90},
    {"id":103,"name":"rahul","marks":83},
    {"id":104,"name":"ram","marks":97},
    {"id":105,"name":"rakesh","marks":72},
]
with open("myFile.csv","w+",newline="") as file:
    writer = csv.DictWriter(file,fieldnames=["id","name","marks"])
    writer.writeheader()
    writer.writerows(data)
    file.seek(0)
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

