import csv
import json
import time
import requests
i = 1


next_time = time.time()
while True:

    url = "http://random-data-api.com/api/v2/users"
    req = requests.get(url)

    content = json.loads(req.text)

    address_dic = []
    address_dic = (content['address']['street_name']+","+content['address']['street_address'] + "," +
                   content['address']['city']+","+content['address']['state']+","+content['address']['country'])
    fields = ['id', 'FirstName', 'LastName', 'Username',
              'Email', 'Avatar', 'Gender', 'DoB', 'Address']
    data = [content['id'], content['first_name'], content['last_name'], content['username'],
            content['email'], content['avatar'], content['gender'], content['date_of_birth'], address_dic]
    with open('/home/norman/Documents/csvproject/users.csv', 'a') as f_obj:

        writer_obj = csv.writer(f_obj)
        if (i == 1):
            writer_obj.writerow(fields)
        writer_obj.writerow(data)
        i += 2

    next_time += 1
    time.sleep(max(0, next_time - time.time()))
