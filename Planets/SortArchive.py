import csv 
data = []
with open ("archive_dataset.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)
headers = data[0]
planet_data = data[1:]
for d in planet_data:
    d[2] = d[2].lower()
planet_data.sort(key=lambda planet_data:planet_data[2])
with open ("sorted_archive_dataset.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)
with open ("sorted_archive_dataset.csv", "r") as input,open("sorted1_archive_dataset.csv", "a+", newline='') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if(any (field.strip() for field in row)):
            writer.writerow(row)



    