"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


phone_numbers = []

for data in texts:
    phone_numbers.extend(data[:2])
for data in calls:
    phone_numbers.extend(data[:2])

unique_num_cnt = len(set(phone_numbers))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

print(
    f"""
    There are {unique_num_cnt} different telephone numbers in the records.
    """
    )