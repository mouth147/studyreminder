# Daily Reminders

This is a daily reminder script that texts me to study some of my data structures/algorithms.

# Installation

1. You need to install the Twilio Rest Client ```pip install twilio```
2. Edit the account-example.py with Twilio credentials and the right phone numbers and resave it as account.py
3. To run it on a daily basis edit your crontab by entering into your terminal ```crontab -e``` then ```00 10 * * * /path/to/script python reminder.py``` The following will text you everyday at 10:00am
