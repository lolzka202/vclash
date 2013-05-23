# this script will open a file with email addresses in it, then extract
# those address and write them to a new file
import os
import re
# vars for filenames
filename = 'C:\Users\User\Desktop\Export CSV Files\email_entry.txt'
newfilename = 'C:\Users\User\Desktop\Export CSV Files\emaillist-rev.txt'
# read file
if os.path.exists(filename):
    data = open(filename, 'r')
    bulkemails = data.read()
else:
    print("File not found.")
    raise SystemExit
# regular expressions
r1 = re.compile(r'([\w+][\S]+@+\S+\w+)')
results1 = r1.findall(bulkemails)
emails = ""
for x in results1:
    emails += str(x) + "; "
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