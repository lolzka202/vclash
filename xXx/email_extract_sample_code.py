import re
import os
import codecs
from optparse import OptionParser

#=================================================
print 'Email extractor using regex'
Parser = OptionParser()
Parser.add_option('--dump',
                  help='Your email dump',
                  metavar='X')
(Opts, Args) = Parser.parse_args()
Opts = vars(Opts)
if (Opts['dump'] is None):
    print 'Nothing given!'
    exit()
#=================================================
if (os.path.isfile(Opts['dump']) == False):
    print '%s is not a file :(' % Opts['dump']
    exit()
#=================================================
EmailCount = 0
Line = ''
EmailRegex = re.compile('[\w+_\-\.]+@\w[.-0-9a-zA-Z]*\.\w{2,4}')
Dump = file(Opts['dump'], 'r')
Emails = codecs.open('C:\Users\User\Desktop\Export CSV Files\email_entry.txt', 'w', 'utf-8')
for Line in Dump:
    EmailList = re.findall(EmailRegex, Line)
    if (len(EmailList) >= 1):
        for Email in EmailList:
            if (Email != ''):
                Emails.write(Email + '\r\n')
                EmailCount = EmailCount + 1
Emails.close()
Dump.close()
print 'Found %d emails in %s' % (EmailCount, Opts['dump'])
#=================================================

#source site:
# - http://evilzone.org/scripting-languages/(python)-email-extractor/
# - http://9v.lt/projects/python/emailextract.py