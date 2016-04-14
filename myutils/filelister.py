__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

#from os import listdir
#from os.path import isfile, join
import os
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def listfiles(dir):
    return os.listdir(dir)

'''
#Test codes below

files = listfiles("C:/Users/dipesh/Desktop/testfolder")
print(files)
'''