# basic script to remind me to keep up with my data structures and applications
import random
from twilio.rest import TwilioRestClient
from account import ACCOUNT_SID, AUTH_TOKEN, to_number, from_number

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

structures = ['Linked Lists', 'Heaps', 'Trees', 'Binary Trees', 'AVLs', 'Graphs', 'Heapsort',
             'Mergesort', 'Treesort', 'Dijkstras', 'Binary Search', 'Binary Search Trees',
             'Radixsort','Queues', 'Stacks', 'Hash Tables', 'Quicksort']

message = 'Daily Reminder to study!\n'
message += 'Today work on: ' + structures[random.randint(0, len(structures) - 1)] + '\n'

x = random.randint(0,3)
if x == 0:
    message += "No applications for you today :)"
else:
    message += 'Apply for ' + str(x) + ' applications today.'

text = client.messages.create(to=to_number, from_=from_number,
                              body=message)

print 'Daily reminder sent!'
