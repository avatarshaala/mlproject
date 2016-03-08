__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
def updatefrequency(table, key):
    if key in table:
        table[key] += 1
    else:
        table[key] = 1
    return table