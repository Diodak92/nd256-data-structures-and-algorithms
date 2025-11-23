"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

max_call_length = None
ph_num = None
ph_call_dict = {}

for data in calls:
    ph_call_dict[data[0]] = ph_call_dict.get(data[0], 0) + int(data[-1])
    ph_call_dict[data[1]] = ph_call_dict.get(data[1], 0) + int(data[-1])

ph_num, max_call_length = max(ph_call_dict.items(), key=lambda x : x[1])

#print(sorted(list(ph_call_dict.values())))

print(f"{ph_num} spent the longest time, {max_call_length} seconds, on the phone during September 2016")
