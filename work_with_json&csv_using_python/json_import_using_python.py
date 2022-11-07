import json
from time import timezone

# json_file = open('timezones.json')
# json_data = json.load(json_file)
# # print(json_data)
# for i in json_data:
#     print(i)
#
#json_file.close()
#
#

json_file = open('timezones.json', "r")
json_data = json.loads(json_file.read())

for i in json_data:
    print(i)

json_file.close()

#
# with open('timezones.json') as json_file:
#     data = json.dumps(json_file)
#
# print(data)
#
