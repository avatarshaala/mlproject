__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''


def append_bias_vector(target, biasesvect):
	i = 0
	for bias in biasesvect:
		[bias] + target[i] #append in front of target
		i+=1
	return target