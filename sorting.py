import pandas as pandasForSortingCSV
csvData = pandasForSortingCSV.read_csv(
    "/home/norman/Documents/csvproject/users.csv")
csvData.sort_values(['FirstName'], axis=0, ascending=[True], inplace=True)
csvData.to_csv('users-sorted.csv')
