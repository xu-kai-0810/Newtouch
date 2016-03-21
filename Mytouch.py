#!/usr/bin/env python
#coding=utf-8
import os
from sys import argv
print 'current dir ====> ', os.getcwd()
script, newfile = argv
header_msg = {
            'py': '#!/usr/bin/env python\n#coding=utf-8\n',
            'c': '#include<stdio.h>\n'
            }

if len(newfile.split('.')) == 2:
    newfile_type = newfile.split('.')[-1]
    if os.path.exists(os.getcwd()+'/'+newfile):
        print '\tfile already exists...'
    elif newfile_type in header_msg:
        f = open(newfile, 'w')
        print '\tadding header msg...'
        f.write(header_msg[newfile_type])
        f.close()
        print '\tcreated ', newfile
    else:
        temp = open(newfile, 'w')
        temp.close()
        print '\tcreated ', newfile

