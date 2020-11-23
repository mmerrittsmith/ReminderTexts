# ReminderTexts


This project was inspired by a desire to continually reassure those I love and my own forgetfulness. 

It is a framework I use to send text reminders to myself and others at regular intervals or times. It uses launchd on my laptop to call a Python script that uses the Twilio API to send the desired recipient a SMS with a particular message. 

I have kept my config file off of this repo to protect my privacy, but it contains:

1. My Twilio SID, titled "SID"
2. My Twilio token, titled "TWILIO_TOKEN"
3. My Twilio number, titled "TWILIO_NUMBER"
4. A dictionary of messages, titled "MESSAGES"
5. A dictionary of phone numbers, titled "RECIPIENTS"

Creating this file for yourself should allow you to use this repo just as effectively.
