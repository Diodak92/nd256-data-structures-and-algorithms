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

numbers = []

for num in texts:
    numbers.extend(texts[num[:2]])
for num in calls:
    numbers.extend(calls[num[:2]])

unique_num_cnt = len(set(numbers))

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