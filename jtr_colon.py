#/usr/bin/env python

import sys

if len(sys.argv) !=2:
    print("")
    print("Usage: ./jtr_colon.py FILENAME")
    print("First run: john --show > FILENAME")
    print("")
    exit()

try:
    jtr_file = open(sys.argv[1], 'r')
except Exception as WHAT:
    print("Unable to open file " + sys.argv[1])
    print WHAT

print("")
for line in jtr_file:
    colons = line.count(':')
    if line.strip() == "":
        pass
    elif 'password hashes cracked,' in line:
        pass
    elif colons !=7:
        extra = colons - 6
        print line.strip()
        user = line.split(':')[0]
        print ("Username: " + user)

        x=1
        final = ""
        while (x <= extra):
            final = final + line.split(':')[x] + ":"
            x=x+1
        print ("Password: " + final[:-1])
        print("")

jtr_file.close()
