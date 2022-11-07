import json
import csv

# opening JSON file and loading the data into the variable data
with open('timezones.json') as json_file:
    json_data = json.load(json_file)

timezone_data = json_data

# open a file for write csv data
data_file = open('timezones.csv', 'w')

# create csv writer object
csv_writer = csv.writer(data_file)

# counter variable for writing headers to the csv file
count = 0

for timezone in timezone_data:
    if count == 0:
        header = timezone.keys()
        csv_writer.writerow(header)
        count += 1

    # writing data in a csv file
    csv_writer.writerow(timezone.values())
data_file.close()
