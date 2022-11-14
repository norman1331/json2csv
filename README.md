# JSON2CSV : JSON TO CSV GENERATOR USING API

This tool consists of three functions:

(a) `randomuser.py` generates a CSV file consisting of every entry from GET request of API.

(b) `searchcsv.py` searches through id of user and filters results on the terminal window.

(c) `sorting.py` sorts and generates a CSV file which is a sorted file on the basis of FirstName of all users.

### Usage

How to use this tools:

- The tools requires following libraries : `requests` and `pandas`.

To install these dependencies:

`pip install -r requirements.txt`

<hr>
<hr>

### Sample Usage:

To run script which generates CSV file from API , type following:

` python3 randomuser.py`

A new CSV file will be generated named ` users.csv` in the installation folder.

<hr>

To read `users.csv` file and generate individual entry on terminal, type the following:

` python3 searchcsv.py`
The result will be displayed if the id is valid and present in csv.

<hr>
To run script which generates a sorted CSV file on FirstName basis, type following:

`python3 sorting.py`

A new CSV file will be generated named `users-sorted.csv` in the installation folder.

## Output:

- These scripts generates two <b>CSV</b> files:
  (a) `users.csv`
  (b) `users-sorted.csv`

## License & Versioning

This tool is licensed under MIT license. The version of the tool is v0.1.0.

## Credits

Credits to random-data api for providing free access to their APIs.
Credits to AdvancedWare for providing me the opportunity to work on this project.
