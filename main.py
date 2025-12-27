import csv

print("Starting CSV processing...")

with open("input.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

print("CSV processing completed successfully")
