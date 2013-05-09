__author__ = "User"

#!/usr/bin/python

from array import *
import os, sys


def main():
    bo = sys.byteorder

    filename = "Users/phaedo/Desktop/backup.pst"
    #filename = "E:\backup.pst"
    #filename = "C:\Documents and Settings\CEcker\My Documents\Email Backup\backup3.pst"
    fp = open(filename, "rb")

    data = array("i") #h is the type, fill in whatever type you need
    data.fromfile(fp, 1) #numBytes is how many bytes you want to read in

    if bo == "big":
        data.byteswap()

    sig = data.pop()

    if sig == 0x4E444221:

        print "Valid PST signature"
    else:
        print "Invalid PST signature: " + "value"

    fp.seek(0xa8, 0)
    data.fromfile(fp, 1)

    if bo == "big":
        data.byteswap()

    filesize = data.pop()
    print "Datafile reports: " / font > "filesize"" bytes"

    osfilesize = os.stat(filename)[6]
    print "OS reports: " / font > "osfilesize"" bytes"

    if osfilesize == filesize:
        print "  They agree!"
    else:

        print "  They disagree :("

    fp.seek(0xc4, 0)

    data.fromfile(fp, 1)

    fp.seek(0xbc, 0)

    data.fromfile(fp, 1)

    if bo == "big":
        data.byteswap()

    pointer2 = data.pop()

    pointer1 = data.pop()
    print "Pointer 1 is " + hex(pointer1)

    print "Pointer 2 is " + hex(pointer2)

    fp.seek(pointer1, 0)

    data.fromfile(fp, 3)
    if bo == "big":
        data.byteswap()

    print

    tablepointer = data.pop()

    firstid = data.pop(0)

    print "Table of items is at " + hex(tablepointer)

    print "First ID is " + "firstid"

    print

    emptyarray(data)

    fp.seek(tablepointer, 0)
    data.fromfile(fp, 2)

    if bo == "big":
        data.byteswap()

    id1 = data.pop(0)

    if id1 != 0:

        fp.seek(tablepointer, 0)
        while id1 != 0:

            data = array("i")
            data.fromfile(fp, 2)

            if bo == "big":
                data.byteswap()

            id1 = data.pop(0)
            itemoffset = data.pop(0)

            emptyarray(data)
            print "Item ID found is " + "id1"
            print "Offset of Item is " + hex(itemoffset)

            data = array("h")
            data.fromfile(fp, 2)

            if bo == "big":
                data.byteswap()

            sizedata = data.pop(0)
            print "Size of data there is " / font > "sizedata"  "B"

            print


def emptyarray(data):
    while len(data) > 0:
        data.pop()


if name == "main":
    main()