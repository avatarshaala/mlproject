#__author__ = 'dipesh'
from functions.activations import signed_unit
from myutils.vectorutil import vectequals, dotprod

__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

import random

def generate_bias_vector(n):
	return [1]*n

def generate_weights(n):
	return [random.random() for i in range(n)]


def sse(values, golds):
	sse = 0
	n = 0
	for value in values:
		sse += pow(value-golds[n],2)
		n += 1
	return sse/n
    #return pow(sse/n,0.5)


def get_output(input, weights):
	val = signed_unit(dotprod(input, weights))
	return val

def train(instances, targets, alpha, iterations, initial_weights=[], stop_after_convergence=True):

	weights = initial_weights
	n = len(instances[0])
	if not weights:
		weights = generate_weights(n+1)
	message = "Training normally completed in {} iterations without convergence during iterations".format(iterations)
	#iterate iterations time
	for itr in range(1, iterations+1):
		oldweights = list(weights)
		#iterate through each instance
		for i in range(0, len(instances)):
			output = get_output(instances[i], weights)
			#update each weight by using formula wj = wj + alphs * (ti-oi)*xj
			for j in range(0,n):
				weights[j] = weights[j]  + alpha * (targets[i]-output)*instances[i][j]

		if vectequals(oldweights,weights):
			message = "Training converged after {} iterations and continued iterations".format(itr)
			#check convergence
			if stop_after_convergence:
				message = "Training converged after {} iterations and stopped iterations".format(itr)
				break
	return weights, message

def test(weights, instance):
	return get_output(instance, weights)


