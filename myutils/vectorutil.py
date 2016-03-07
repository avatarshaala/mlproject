__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''


def vectequals(v1,v2):
	for i in range(0,len(v1)):
		if not(v1[i] == v2[i]):
			return False
	return True


def dotprod(v1,v2):
    val = 0
    n = 0
    for x in v1:
        val+= x * v2[n]
        n+=1
    return val