#! /usr/bin/env python

import os
import glob

file_names = glob.glob('DCP*.py')

for file_name in file_names:
    os.system('git add ' + '"' + file_name + '"')
    if '!' in file_name:
        os.system('git commit -m "Uncomplete"')
    else:
        os.system('git commit -m "Complete"')
        


