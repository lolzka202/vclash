# this script will open a file with email addresses in it, then extract 
# those address and write them to a new file

import os
import re

# vars for filenames (rename the location of files with email entry)
filename = 'C:\Users\User\Desktop\Export CSV Files\email_entry1.txt'
newfilename = 'C:\Users\User\Desktop\Export CSV Files\emaillist-rev.txt'

# read file
if os.path.exists(filename):
    data = open(filename, 'r')
    bulkemails = data.read()
else:
    print "File not found."
    raise SystemExit

# use the email python expression --> (r'([\w+][\S]+@+\S+\w+)') <--- to be fully work
# original expression applied ---> (r'(\b[\w.]+@+[\w.]+.+[\w.]\b)')

# ('^(?P<name>[A-Za-z ]+)<(?P<email>[^ ]+@[^.]+\.[\w.]+)>$') - not working
# source: http://stackoverflow.com/questions/8116441/validate-name-surname-emailexample-com-using-regex-in-python-django
# re-encoded regex --> (r'([A-Za-z ]+)<([\w+][\S]+@+\S+\w+)>') from email_extract_test.py
# another working regex ---> <([\w\.=-]+@[\w\.-]+\.[\w]{2,3})>

# Pattern title --> ([A-Za-z ]+)<([\w\.=-]+@[\w\.-]+\.[\w]{2,10})>
# Matches	a@a.com | a@a.com.au | a@a.au // Non-Matches	word | word@ | @word

r = re.compile(r'([A-Za-z ]+)<([\w+][\S]+@+\S+\w+)>')
results = r.findall(bulkemails)

emails = ""
for x in results:
    emails += str(x) + "\n"

# function to write file
def writefile():
    f = open(newfilename, 'w')
    f.write(emails)
    f.close()
    print "File written."

# function to handle overwrite question
def overwrite_ok():
    response = raw_input("Are you sure you want to overwrite " + str(newfilename) + "? Yes or No\n")
    if response == "Yes":
        writefile()
    elif response == "No":
        print "Aborted."
    else:
        print "Please enter Yes or No."
        overwrite_ok()

# write/overwrite
if os.path.exists(newfilename):
    overwrite_ok()
else:
    writefile()