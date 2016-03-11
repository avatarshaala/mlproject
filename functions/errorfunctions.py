__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''


def sse(values, golds):
		sse = 0
		n = 0
		for value in values:
			sse += pow(value-golds[n],2)
			n += 1
		return sse/n