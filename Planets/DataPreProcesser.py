import csv
b1 = []
b2 = []
with open ("final.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        b1.append(row)
with open ("sorted1_archive_dataset.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        b2.append(row)
header1 = b1[0]
header2 = b2[0]
planet_data1 = b1[1:]
planet_data2 = b2[1:]
headers = header1+header2
planet_data = []
for index, row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])
with open ("merged_dataset.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)
        

