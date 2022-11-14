import sys
import csv
filename = "users_record.csv"
id_user = input('Enter id of user\n')
csv_file = csv.reader(
    open('/home/norman/Documents/csvproject/users.csv', "r"), delimiter=",")
for row in csv_file:
    if id_user == row[0]:
        print(row)
