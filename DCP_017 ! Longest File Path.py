"""
This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 
    and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext
            \n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2
            \n\t\t\tfile2.ext" 
            represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. 
subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. 
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) 
    absolute path to a file within our file system. 
    For example, in the second example above, 
    the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", 
    and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, 
return the length of the longest absolute path to a file in the abstracted file system. 
If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
"""
from collections import defaultdict
def longest_file_path(dir):
    if dir.count('.') == 0:
        return 0
    directory = dir
    subdirfiles = directory.count('\n')
    tabs = directory.count('\t')

    longest_directory_depth = 0
    dir_search = '\n\t'
    while directory.count(dir_search) > 0:
        longest_directory_depth += 1
        dir_search += '\t'
    print(longest_directory_depth)
    
    print(subdirfiles, tabs)
    directory = directory.split('\n')
        

    print(directory)
    x = 0
    while x < len(directory):
        if '.' not in directory[x]:
            print(directory[x])
            del directory[x]
        else:
            x += 1
    print(directory)


directory = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 

print(longest_file_path(directory))