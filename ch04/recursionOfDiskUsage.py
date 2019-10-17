# Kelvin modified on Sep 18, 2019
#

import os

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendents."""
    total = os.path.getsize(path)                       # account for direct usage
    if os.path.isdir(path):                             # if this is a directory,
        for filename in os.listdir(path):               # then for each child:
            childpath = os.path.join(path, filename)    # compose full path to child
            total += disk_usage(childpath)              # add child's usage to total

    print('{0:<8}'.format(total), path)                  # descriptive output (optinal)
    #print (total, path)                                 # Test: scenario without format 
    return total

if __name__ == '__main__':
    mypath = "/Users/Algorithms"
    disk_usage(mypath)