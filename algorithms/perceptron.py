#__author__ = 'dipesh'
from functions.activations import signed_unit
from myutils.vectorutil import vectequals, dotprod

__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
#return pow(sse/n,0.5)
import random
class perceptron:
	def __init__(self):
		self.__weights__ = []

	def generate_bias_vector(self,n):
		return [1]*n

	def generate_weights(self,n):
		return [random.random() for i in range(n)]

	def get_output(self,input, weights):
		val = signed_unit(dotprod(input, weights))
		return val

	def train(self,instances, targets, alpha, iterations, initial_weights=[], stop_after_convergence=True):

		#global __weights__
		self.__weights__ = initial_weights
		n = len(instances[0])
		if not self.__weights__:
			self.__weights__ = self.generate_weights(n+1)
		message = "Training normally completed in {} iterations without convergence during iterations".format(iterations)
		#iterate iterations time
		for itr in range(1, iterations+1):
			oldweights = list(self.__weights__)
			#iterate through each instance
			for i in range(0, len(instances)):
				output = self.get_output(instances[i], self.__weights__)
				#update each weight by using formula wj = wj + alphs * (ti-oi)*xj
				for j in range(0,n):
					self.__weights__[j] = self.__weights__[j]  + alpha * (targets[i]-output)*instances[i][j]

			if vectequals(oldweights,self.__weights__):
				message = "Training converged after {} iterations and continued iterations".format(itr)
				#check convergence
				if stop_after_convergence:
					message = "Training converged after {} iterations and stopped iterations".format(itr)
					break
		return self.__weights__, message

	def test(self,instance):
		#global __weights__
		return self.get_output(instance, self.__weights__)


