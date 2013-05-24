import re

# Open file
f = open('C:\Users\User\Desktop\Export CSV Files\email_entry1.txt', 'r')
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall(r'([A-Za-z ]+)<(\b[\w.]+@+[\w.]+.+[\w.]\b)>', f.read())

for results in strings:
    print results