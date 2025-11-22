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

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Telemarketers
text_senders = []
text_receivers = []
phone_callers = []
phone_receivers = []
telemarketers = []

for data in texts:
    if data[0] not in text_senders:
        text_senders.append(data[0])
    if data[1] not in text_receivers:
        text_receivers.append(data[1])

for data in calls:
    if data[0] not in phone_callers:
        phone_callers.append(data[0])
    if data[1] not in phone_receivers:
        phone_receivers.append(data[1])

for caller in phone_callers:
    if (caller not in text_senders) and (caller not in text_receivers) and (caller not in phone_receivers):
        telemarketers.append(caller)

print("These numbers could be telemarketers: ")
for ph_num in sorted(telemarketers):
    print(ph_num)
